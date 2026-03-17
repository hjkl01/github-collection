import asyncio
import re
import sys
from pathlib import Path

from api.config import logger
from api.prompts import MARKDOWN_PROMPT
from api.api_ai import auto_category, api_openai_generate, api_github_readme
from api.github_trending_scraper import main as github_trending_scraper


def extract_github_info(github_url):
    pattern = r"https?://github\.com/([^/]+)/([^/?#]+)(?:[/?#].*)?"
    match = re.search(pattern, github_url.strip())
    if match:
        username = match.group(1)
        project_name = match.group(2)
        return username, project_name
    else:
        return None, None


def list_files(dirname="docs"):
    return [str(p) for p in Path(dirname).rglob("*") if p.is_file()]


async def process_single_url(project_line, md_files):
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
        readme_content = await api_github_readme(username, repository)
        if readme_content is None:
            return None
        prompt = MARKDOWN_PROMPT.replace("readme_content", readme_content)
        ai_resp = await api_openai_generate(prompt)
        if isinstance(ai_resp, dict):
            ai_resp = ai_resp.get("text", "")

        if "<think>" in ai_resp or "</think>" in ai_resp:
            ai_resp = re.sub(r".*</think>", "", ai_resp, flags=re.DOTALL).strip()

        if len(temp) == 1:
            category_dir = "00"
        elif len(temp) == 2:
            category_dir = temp[1]
        else:
            logger.info(f"无法解析：{temp}")
            return None

        title = """### [username repository](https://github.com/username/repository)  ![GitHub Repo stars](https://img.shields.io/github/stars/username/repository?style=social)

"""
        text = title.replace("username", username).replace("repository", repository) + ai_resp

        category_path = Path(f"docs/{category_dir}")
        category_path.mkdir(parents=True, exist_ok=True)

        with open(category_path / filename, "w") as file:
            file.write(text)

        return f"Created: {filename}"

    except Exception as e:
        logger.error(f"处理项目 {url} 时出错：{str(e)}")
        return None


async def category_md_files(dirname="docs/00"):
    if not Path(dirname).exists():
        logger.warning(f"dirname not exists {dirname}")
        return

    category_dirs = [str(child.relative_to(Path("docs"))) for child in Path("docs").iterdir() if child.is_dir()]

    md_files = list(Path(dirname).glob("*.md"))

    for md_file in md_files:
        content = md_file.read_text(encoding="utf-8")
        category = await auto_category(content, [str(d) for d in category_dirs])
        logger.info(f"{md_file.name}, {category}")
        if category in category_dirs:
            target = Path("docs") / category / md_file.name
            target.parent.mkdir(parents=True, exist_ok=True)
            md_file.rename(target)
            logger.debug(f"Moved to {target}")

    if Path(dirname).exists():
        import shutil

        shutil.rmtree(dirname)


async def main(args=None):
    if args == "cate":
        await category_md_files()
        return

    with open("urls.txt", "r", encoding="utf-8") as f:
        urls = f.readlines()

    md_files = list(set(f.split("/")[-1] for f in list_files()))

    tasks = [process_single_url(line, md_files) for line in urls]
    results = await asyncio.gather(*tasks)

    success = [r for r in results if r]
    logger.info(f"处理完成: {len(success)} 成功, {len(urls) - len(success)} 跳过/失败")

    await category_md_files()


def export_urls():
    md_files = list(Path("docs").rglob("*.md"))
    md_files.extend(list(Path("docs").rglob("*.mdx")))

    url_folders: dict[str, set] = {}
    github_pattern = re.compile(r"https://github\.com/([a-zA-Z0-9_-]+)/([a-zA-Z0-9_-]+)")

    for md_file in md_files:
        try:
            content = md_file.read_text(encoding="utf-8")
            matches = github_pattern.findall(content)
            rel_path = md_file.relative_to(Path("docs"))
            folder = rel_path.parts[0] if len(rel_path.parts) > 1 else ""
            for username, repo in matches:
                url = f"https://github.com/{username}/{repo}"
                if url not in url_folders:
                    url_folders[url] = set()
                if folder:
                    url_folders[url].add(folder)
        except Exception as e:
            logger.warning(f"读取文件失败 {md_file}: {e}")

    with open("bak.txt", "a", encoding="utf-8") as f:
        for url, folders in sorted(url_folders.items()):
            folder_str = " ".join(sorted(folders)) if folders else ""
            line = f"{url} {folder_str}".strip()
            f.write(line + "\n")

    logger.info(f"导出完成: 共 {len(url_folders)} 个 URL")


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) > 1 and argv[1] == "cate":
        asyncio.run(main("cate"))
    elif len(argv) > 1 and argv[1] == "crawl":
        github_trending_scraper()
    elif len(argv) > 1 and argv[1] == "export":
        export_urls()
    else:
        asyncio.run(main())
