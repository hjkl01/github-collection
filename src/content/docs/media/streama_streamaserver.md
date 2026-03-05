
---
title: streama
---

### [streamaserver streama](https://github.com/streamaserver/streama)  ![GitHub Repo stars](https://img.shields.io/github/stars/streamaserver/streama?style=social)

Streama 是一个个人流媒体服务器项目，用于帮助用户整理并观看自有的电影和电视剧集，提供类似 Netflix 的观影体验。

核心功能包括：
1. **媒体管理**：集成 TMDB API 自动获取元数据与封面，支持视频拖拽上传、本地文件映射及基于正则表达式批量导入。
2. **播放功能**：基于 HTML5 的播放器，支持断点续播、观看进度同步及类似 Netflix 的集数/季数浏览界面。
3. **用户系统**：支持多用户账户管理、权限分配（管理员/普通用户）及邀请功能。
4. **技术架构**：后端采用 Grails 3 构建 REST API，前端使用 AngularJS，依赖浏览器兼容性无需服务器端视频转码。