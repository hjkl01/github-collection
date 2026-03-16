import asyncio
import re
import os
from crawlee.crawlers._beautifulsoup import BeautifulSoupCrawler


async def scrape_github_trending():
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
                repo_name = href_str.strip("/")
                repo_url = f"https://github.com{href_str}"

                desc_elem = article.find("p", class_="col-9")
                description = desc_elem.text.strip() if desc_elem else ""

                lang_elem = article.find("span", itemprop="programmingLanguage")
                language = lang_elem.text.strip() if lang_elem else ""

                stats = article.find_all("a", class_="Link--muted")
                stars = ""
                forks = ""
                for stat in stats:
                    href_stat = stat.get("href", "")
                    if href_stat and "stars" in href_stat:
                        stars = stat.text.strip()
                    elif href_stat and "forks" in href_stat:
                        forks = stat.text.strip()

                today_stars_elem = article.find("span", class_="d-inline-block float-sm-right")
                today_stars = today_stars_elem.text.strip() if today_stars_elem else ""

                repo_info = {
                    "name": repo_name,
                    "url": repo_url,
                    "description": description,
                    "language": language,
                    "stars": stars,
                    "forks": forks,
                    "today_stars": today_stars,
                }
                repos.append(repo_info)

            except Exception as e:
                print(f"Error parsing repo: {e}")
                continue

    crawler = BeautifulSoupCrawler()
    crawler.router.default_handler(handler)

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


def extract_github_info(github_url):
    pattern = r"https?://github\.com/([^/]+)/([^/?#]+)(?:[/?#].*)?"

    match = re.search(pattern, github_url.strip())

    if match:
        username = match.group(1)
        project_name = match.group(2)
        return username, project_name
    else:
        return None, None


def main():
    trending_repos = asyncio.run(scrape_github_trending())
    if not os.path.exists("urls.txt"):
        os.system("touch urls.txt")
    with open("./urls.txt", "r") as f:
        old_urls = [u.strip() for u in f.readlines()]
    urls = list(set([trending_repo["url"] for trending_repo in trending_repos]))
    for url in urls:
        if url not in old_urls:
            with open("./urls.txt", "a") as f:
                f.write(f"{url}\n")

    print("Data saved to urls.txt")


if __name__ == "__main__":
    main()
