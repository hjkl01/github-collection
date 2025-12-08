
---
title: GoFilm
---

### [ProudMuBai GoFilm](https://github.com/ProudMuBai/GoFilm)

GoFilm 是一个基于 Vue（前端）和 Gin（后端）构建的在线观影网站，支持影视资源采集、定时更新和管理功能。项目采用 Vite + Vue + ElementPlus 作为前端技术栈，后端使用 Gin + gorm + go-redis 框架，通过 gocolly 和 robfig/cron 实现资源采集与定时任务。  

**主要功能**：  
- 支持前台影片浏览、搜索、分类查看及播放；  
- 管理后台可配置采集站点、定时任务、影片分类及基本信息；  
- 新增移动端观看历史、采集失败重试机制、Banner 参数修改等功能；  
- 提供 Docker 部署方案及 1Panel 可视化部署指南。  

**使用方式**：  
- 前端代码位于 `client` 目录，后端代码位于 `server` 目录，部署文件在 `film` 目录；  
- 默认访问地址：`http://服务器IP:端口`（前台）和 `http://服务器IP:端口/manage`（后台）；  
- 管理后台默认账号密码为 `admin/admin`，首次登录后需修改密码。  

**特性亮点**：  
- 支持定时更新影视资源及失败采集重试；  
- 前台与后台数据联动，可动态修改网站信息；  
- 提供详细的部署文档及使用说明，包含 Docker 部署流程。