
---
title: csghub-server
---

### [OpenCSGs csghub-server](https://github.com/OpenCSGs/csghub-server)  ![GitHub Repo stars](https://img.shields.io/github/stars/OpenCSGs/csghub-server?style=social)

CSGHub Server 是大模型资产开源管理平台 CSGHub 的核心服务端组件，通过 REST API 实现模型、数据集等 LLM 资产的全面管理。主要功能包括：

1. **用户与组织管理**：支持用户和组织的创建与管理。
2. **资产检索与标签**：支持多实体搜索，提供模型和数据的自动打标及定制元数据功能。
3. **文件管理与预览**：支持数据集文件（如.parquet）在线预览及文件（含 LFS）下载。
4. **安全与监控**：提供文本和图像内容审核，跟踪下载、点赞等活跃度数据。
5. **灵活扩展**：兼容多种 Git 服务器（如 Gitea），支持 S3 协议存储，可按需集成第三方内容审核服务，支持模型一键部署。