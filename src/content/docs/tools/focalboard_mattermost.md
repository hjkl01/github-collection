
---
title: focalboard
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/mattermost/focalboard?style=social) ](https://github.com/mattermost/focalboard)
### [mattermost focalboard](https://github.com/mattermost/focalboard)

**核心内容总结：**  
Focalboard 是一款开源、多语言、自托管的项目管理工具，支持替代 Trello、Notion 和 Asana。提供两种版本：  
1. **个人桌面版**：支持 macOS、Windows 和 Linux 的单机应用，用于个人任务管理。  
2. **个人服务器版**：支持多用户部署，适用于开发和私人使用。  

**使用方法**：  
- **桌面版**：通过应用商店或 GitHub 发布页面下载安装包，解压后运行即可。  
- **服务器版**：按官方指南在 Ubuntu 上安装。  
- **开发**：需创建 `.env` 文件（设置 `EXCLUDE_ENTERPRISE="1"`），通过 `make prebuild` 和 `make` 构建服务器，运行 `./bin/focalboard-server` 启动服务。  

**主要特性**：  
- 支持多平台（Windows、macOS、Linux、Docker）。  
- 提供 API 文档及开发者指南。  
- 支持通过 Docker 镜像快速部署。  
- 包含单元测试、ESLint 和 UI 测试流程。  

**注意事项**：  
- 项目当前未维护，需通过指定链接申请成为维护者。  
- 若需 Mattermost 插件，请参考其他仓库。