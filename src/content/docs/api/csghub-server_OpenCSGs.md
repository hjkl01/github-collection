
---
title: csghub-server
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/OpenCSGs/csghub-server?style=social) ](https://github.com/OpenCSGs/csghub-server)
### [OpenCSGs csghub-server](https://github.com/OpenCSGs/csghub-server)

**项目核心内容总结：**  
CSGHub Server 是 CSGHub 平台的核心组件，用于通过 REST API 管理大模型（LLM）资产，包括模型、数据集等。  

**主要功能：**  
- 用户与组织管理、模型/数据集自动标签、多维度搜索（用户、组织、模型、数据）；  
- 支持 `.parquet` 等格式的数据集在线预览、文本与图像内容审核；  
- 提供文件下载（含 LFS 大文件）、模型/数据集活动数据追踪（如下载量、点赞数）。  

**使用方法：**  
- 系统要求：4 核 CPU / 8GB 内存，需安装 Docker；  
- 通过 `docker-compose` 部署，配置 API Token 后运行命令启动服务；  
- 支持 TOML 格式配置文件，提供本地启动和部署选项。  

**技术特性：**  
- 支持 Gitea、GitLab 等多 Git 服务器，兼容 S3 协议的存储（如 MinIO）；  
- 可扩展集成第三方内容审核服务，支持模型一键部署与推理。  

**许可证：** 采用 Apache 2.0 协议。