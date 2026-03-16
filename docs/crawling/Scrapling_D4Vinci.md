### [D4Vinci Scrapling](https://github.com/D4Vinci/Scrapling)  ![GitHub Repo stars](https://img.shields.io/github/stars/D4Vinci/Scrapling?style=social)

Scrapling 是一个自适应的 Web 抓取框架，支持从单次请求到大规模爬取。

- **自适应解析**：智能追踪元素，自动适应网站结构变更，持续定位目标内容。
- **高级抓取**：内置绕过反爬虫系统（如 Cloudflare Turnstile）能力，支持 HTTP、动态页面浏览器自动化及隐身模式。
- **爬虫框架**：类似 Scrapy 的 API，支持高并发、多会话、暂停/恢复、自动代理轮换及数据流输出。
- **高性能**：极速抓取，低内存占用，JSON 序列化速度快于标准库。
- **AI 集成**：内置 MCP 服务器，辅助 AI 模型进行辅助抓取和内容提取。
- **命令行工具**：提供交互式 Shell 及无需编程的直接抓取命令。

支持 Python 同步/异步模式，兼容 Scrapy 和 BeautifulSoup 风格 API，并提供 Docker 镜像。