
---
title: facebook-scraper
---

### [kevinzg facebook-scraper](https://github.com/kevinzg/facebook-scraper)  ![GitHub Repo stars](https://img.shields.io/github/stars/kevinzg/facebook-scraper?style=social)

这是一个无需 API 密钥即可抓取 Facebook 公开内容的 Python 库及命令行工具。主要功能包括：

1. **帖子抓取**：支持通过用户名、主页/群组 ID 或 URL 获取帖子文本、图片、视频、时间及基础互动数据（点赞、分享）。
2. **深度数据**：可选提取评论、回复、用户反应详情，以及个人资料（教育、工作等）和群组信息（成员数、管理员）。
3. **数据输出**：提供 Python 接口返回结构化数据，支持直接导出为 CSV 或 JSON 文件，具备断点续传及内容过滤功能。
4. **登录增强**：通过 Cookie 登录可解锁更多受限数据（如完整评论、反应统计及管理员列表）。