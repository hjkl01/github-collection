
---
title: web-unified-docs
---

### [hashicorp web-unified-docs](https://github.com/hashicorp/web-unified-docs)  ![GitHub Repo stars](https://img.shields.io/github/stars/hashicorp/web-unified-docs?style=social)

该项目旨在构建统一的产品文档仓库，作为 HashiCorp 产品文档的统一 API 服务源，逐步替代现有内容 API。
1. **统一文档 API**：托管所有产品文档，为 Dev Portal 前端提供内容服务。
2. **断链监控**：在 PR 预览中提示断链信息，生产环境每周扫描并针对用户影响发送警报。
3. **工作流简化**：将文档集中存储于单仓库分支，简化版本管理、跨产品更新及新功能集成。
4. **迁移工具**：提供脚本协助产品文档迁移，并在原文档位置添加迁移指引。
5. **本地开发**：支持通过 Docker 快速搭建本地文档预览环境。