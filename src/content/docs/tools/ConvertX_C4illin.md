
---
title: ConvertX
---

### [C4illin ConvertX](https://github.com/C4illin/ConvertX)  ![GitHub Repo stars](https://img.shields.io/github/stars/C4illin/ConvertX?style=social)

ConvertX 是一个自托管的在线文件转换工具，支持超过 1000 种文件格式，涵盖图像、文档、视频、音频等场景。项目使用 TypeScript、Bun 和 Elysia 开发，主要特性包括批量文件转换、密码保护、多账号支持及转换历史管理。

**部署方式**  
通过 Docker 部署，提供 `docker-compose.yml` 配置或直接运行 `docker run` 命令。需挂载数据卷并设置环境变量（如 `JWT_SECRET` 密钥），默认端口为 3000。若需允许 HTTP 访问或开放注册功能，需修改对应环境变量。

**核心功能**  
- 支持 Inkscape、FFmpeg、LibreOffice 等工具，覆盖图像、文档、视频等格式转换  
- 可配置自动清理旧文件、限制并发转换任务数  
- 提供多语言支持（通过 BCP 47 语言标签）  

**镜像版本**  
GitHub Container Registry 和 Docker Hub 提供 `latest`（稳定版）和 `main`（开发版）两个标签。