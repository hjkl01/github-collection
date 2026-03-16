### [ourongxing newsnow](https://github.com/ourongxing/newsnow)  ![GitHub Repo stars](https://img.shields.io/github/stars/ourongxing/newsnow?style=social)

本项目是一个实时热点新闻阅读应用，旨在提供优雅简洁的阅读体验。核心功能总结如下：

1. **实时资讯聚合**：自动更新热门新闻，采用自适应抓取间隔以优化资源并防止 IP 封禁。
2. **用户系统**：支持 GitHub OAuth 登录与数据同步，提供缓存管理与登录用户强制刷新功能。
3. **MCP 支持**：内置 MCP 服务器配置，支持自定义 BASE_URL。
4. **架构扩展性**：提供清晰的类型定义与架构，便于添加新的数据源，兼容多种数据库（推荐 Cloudflare D1）。
5. **多环境部署**：支持 Cloudflare Pages、Vercel 及 Docker 快速部署。

当前版本为仅支持中文的演示版，后续计划增加多语言支持及个性化功能。