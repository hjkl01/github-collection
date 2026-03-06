
---
title: GoFilm
---

### [ProudMuBai GoFilm](https://github.com/ProudMuBai/GoFilm)  ![GitHub Repo stars](https://img.shields.io/github/stars/ProudMuBai/GoFilm?style=social)

GoFilm 是一个基于 Vue 和 Gin 框架开发的在线观影网站。

**核心功能**
1. **在线观影**：支持影片搜索、播放、详情页展示及移动端观看历史。
2. **资源采集**：利用爬虫自动采集影视资源，支持定时更新及采集失败重试。
3. **后台管理**：提供管理面板，可管理采集站点、定时任务、网站信息、影片分类及数据。
4. **便捷部署**：支持 Docker 及 1Panel 可视化部署。

**技术架构**
- **前端**：Vite + Vue + ElementPlus
- **后端**：Gin + GORM + go-redis
- **其他**：资源采集（gocolly）、定时任务（robfig/cron）