
---
title: facebook-scraper
---

### [kevinzg facebook-scraper](https://github.com/kevinzg/facebook-scraper)  ![GitHub Repo stars](https://img.shields.io/github/stars/kevinzg/facebook-scraper?style=social)

Facebook Scraper 是一个无需 API 密钥即可抓取 Facebook 公开页面、个人主页及群组数据的 Python 库。

核心功能总结：
1. **内容抓取**：获取帖子文本、链接、图片、视频、发布时间及互动数据（点赞、分享）。
2. **互动数据**：支持提取评论、回复、反应类型（如喜欢、喜爱）及反应者信息。
3. **用户与群组信息**：可获取个人资料（教育、工作等）及群组详情（管理员、成员数等）。
4. **数据导出**：支持命令行及 Python 接口，可直接写入 CSV 或 JSON 文件，支持断点续传与关键词过滤。
5. **增强访问**：支持通过 Cookie 登录获取受限信息，可选配合 youtube-dl 提取高清视频。