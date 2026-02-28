import os
import sys
import re
import asyncio
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from functools import partial

from api.config import logger
from api.prompts import MARKDOWN_PROMPT
from api.api_ai import auto_category, api_openai_generate, api_github_readme
from api.github_trending_scraper import main as github_trending_scraper


def clean_small_md_files(dirname="src/content/docs", min_size=200):
    """删除小于指定大小的 md 文件"""
    deleted = []
    for root, dirs, files in os.walk(dirname):
        for file in files:
            if file.endswith(".md"):
                filepath = Path(root) / file
                size = filepath.stat().st_size
                if size < min_size:
                    filepath.unlink()
                    deleted.append(str(filepath))
    if deleted:
        logger.info(f"Deleted {len(deleted)} small files")
    return deleted


def extract_github_info(github_url):
    """
    从GitHub URL中提取用户名和项目名

    Args:
        github_url (str): GitHub仓库URL

    Returns:
        tuple: (username, project_name) 或 (None, None) 如果匹配失败
    """

    # logger.debug(github_url)
    # GitHub仓库URL的正则表达式模式
    pattern = r"https?://github\.com/([^/]+)/([^/?#]+)(?:[/?#].*)?"

    match = re.search(pattern, github_url.strip())

    if match:
        username = match.group(1)
        project_name = match.group(2)
        # logger.debug(f"{username} {project_name}")
        return username, project_name
    else:
        return None, None


def list_files(dirname="src/content/docs"):
    """列出目录下的所有文件"""
    return [str(p) for p in Path(dirname).rglob("*") if p.is_file()]


def process_single_url(project_line, md_files):
    """处理单个 URL，返回结果或 None"""
    project_line = project_line.strip()
    if not project_line:
        return None

    temp = project_line.split(" ")
    url = temp[0]

    username, repository = extract_github_info(url)
    if not username or not repository:
        logger.info(f"无法解析 GitHub URL: {url}")
        return None

    filename = f"{repository}_{username}.md"
    if filename in md_files:
        return None

    logger.info(project_line)
    try:
        readme_content = api_github_readme(username, repository)
        if readme_content is None:
            return None
        prompt = MARKDOWN_PROMPT.replace("readme_content", readme_content)
        ai_resp = api_openai_generate(prompt)
        if isinstance(ai_resp, dict):
            ai_resp = ai_resp.get("text", "")

        # 去除 OpenAI o1 系列模型返回的 think 标签内容
        if "<think>" in ai_resp or "</think>" in ai_resp:
            ai_resp = re.sub(r".*</think>", "", ai_resp, flags=re.DOTALL).strip()

        if len(temp) == 1:
            category_dir = "00"
        elif len(temp) == 2:
            category_dir = temp[1]
        else:
            logger.info(f"无法解析：{temp}")
            return None

        title = """
---
title: repository
---

### [username repository](https://github.com/username/repository)  ![GitHub Repo stars](https://img.shields.io/github/stars/username/repository?style=social)

"""

        text = title.replace("username", username).replace("repository", repository) + ai_resp

        category_path = Path(f"src/content/docs/{category_dir}")
        category_path.mkdir(parents=True, exist_ok=True)

        with open(category_path / filename, "w") as file:
            file.write(text)

        return f"Created: {filename}"

    except Exception as e:
        logger.error(f"处理项目 {url} 时出错：{str(e)}")
        return None


async def category_md_files(dirname="src/content/docs/00"):
    """自动分类 md 文件"""
    if not Path(dirname).exists():
        logger.warning(f"dirname not exists {dirname}")
        return

    category_dirs = [str(child.relative_to(Path("src/content/docs"))) for child in Path("src/content/docs").iterdir() if child.is_dir()]

    md_files = list(Path(dirname).glob("*.md"))

    for md_file in md_files:
        content = md_file.read_text(encoding="utf-8")
        category = await auto_category(content, [str(d) for d in category_dirs])
        logger.info(f"{md_file.name}, {category}")
        if category in category_dirs:
            target = Path("src/content/docs") / category / md_file.name
            target.parent.mkdir(parents=True, exist_ok=True)
            md_file.rename(target)
            logger.debug(f"Moved to {target}")

    # 删除空目录
    if Path(dirname).exists():
        import shutil

        shutil.rmtree(dirname)


async def main(args=None):
    """主函数 - 支持并行处理"""
    clean_small_md_files()
    if args == "cate":
        await category_md_files()
        return

    with open("urls.txt", "r", encoding="utf-8") as f:
        urls = f.readlines()

    md_files = set(f.split("/")[-1] for f in list_files())

    # 使用线程池并行处理 URL（API 调用是 IO 密集型）
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor(max_workers=5) as executor:
        tasks = [loop.run_in_executor(executor, process_single_url, line, md_files) for line in urls]
        results = await asyncio.gather(*tasks)

    success = [r for r in results if r]
    logger.info(f"处理完成: {len(success)} 成功, {len(urls) - len(success)} 跳过/失败")

    await category_md_files()


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) > 1 and argv[1] == "cate":
        asyncio.run(main("cate"))
    elif len(argv) > 1 and argv[1] == "crawl":
        github_trending_scraper()
    else:
        asyncio.run(main())
