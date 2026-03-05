
---
title: weiboSpider
---

### [dataabc weiboSpider](https://github.com/dataabc/weiboSpider)  ![GitHub Repo stars](https://img.shields.io/github/stars/dataabc/weiboSpider?style=social)

本项目是一个 Python 编写的微博爬虫工具，核心功能包括：
1. **数据爬取**：支持批量爬取指定用户（一个或多个）的用户信息（如昵称、性别、所在地等）及微博动态数据（如内容、互动数、发布时间等）。
2. **数据存储**：支持将结果保存为 txt、csv、json 文件，或存入 MySQL、MongoDB、SQLite 数据库。
3. **媒体下载**：支持下载微博中的原创及转发图片、视频和 Live Photo 等媒体资源。
4. **环境配置**：需配置 Cookie 获取访问权限（另有免 Cookie 版本），兼容 Python 2 和 Python 3 环境。
5. **扩展功能**：支持代码个性化定制及配置定期自动爬取。