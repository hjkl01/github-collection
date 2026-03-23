import asyncio
from pathlib import Path

from crawlee.crawlers._beautifulsoup import BeautifulSoupCrawler


async def scrape_github_trending() -> list[dict]:
    """爬取 GitHub Trending 仓库"""
    repos = []

    async def handler(context):
        soup = context.soup
        repo_articles = soup.find_all("article", class_="Box-row")

        for article in repo_articles:
            try:
                h2_elem = article.find("h2", class_="h3")
                if not h2_elem:
                    continue

                repo_link = h2_elem.find("a")
                if not repo_link:
                    continue

                href = repo_link.get("href")
                if not href:
                    continue

                href_str = str(href)
                repo_url = f"https://github.com{href_str}"

                # 描述
                desc_elem = article.find("p", class_="col-9")
                description = desc_elem.text.strip() if desc_elem else ""

                # 编程语言
                lang_elem = article.find("span", itemprop="programmingLanguage")
                language = lang_elem.text.strip() if lang_elem else ""

                # 统计数据
                stars = forks = ""
                for stat in article.find_all("a", class_="Link--muted"):
                    href_stat = stat.get("href", "")
                    if "stars" in href_stat:
                        stars = stat.text.strip()
                    elif "forks" in href_stat:
                        forks = stat.text.strip()

                # 今日 star
                today_stars_elem = article.find("span", class_="d-inline-block float-sm-right")
                today_stars = today_stars_elem.text.strip() if today_stars_elem else ""

                repos.append(
                    {
                        "name": href_str.strip("/"),
                        "url": repo_url,
                        "description": description,
                        "language": language,
                        "stars": stars,
                        "forks": forks,
                        "today_stars": today_stars,
                    }
                )
            except Exception as e:
                print(f"解析仓库失败: {e}")
                continue

    crawler = BeautifulSoupCrawler()
    crawler.router.default_handler(handler)

    # 爬取多个语言分类
    await crawler.add_requests(
        [
            "https://github.com/trending?since=weekly",
            "https://github.com/trending/python?since=weekly",
            "https://github.com/trending/lua?since=weekly",
            "https://github.com/trending/go?since=weekly",
            "https://github.com/trending/rust?since=weekly",
        ]
    )
    await crawler.run()

    return repos


def main() -> None:
    """主函数：爬取并保存到 urls.txt"""
    trending_repos = asyncio.run(scrape_github_trending())

    urls_file = Path("urls.txt")
    if not urls_file.exists():
        urls_file.touch()

    # 读取已有 URL
    old_urls = set(urls_file.read_text().splitlines())

    # 添加新 URL
    new_urls = [repo["url"] for repo in trending_repos]
    updated_urls = old_urls.union(new_urls)

    urls_file.write_text("\n".join(sorted(updated_urls)) + "\n", encoding="utf-8")
    print(f"已保存到 urls.txt，共 {len(updated_urls)} 个 URL")


if __name__ == "__main__":
    main()


# 补充 Path 导入
