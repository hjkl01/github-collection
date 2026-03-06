
---
title: web-unified-docs
---

### [hashicorp web-unified-docs](https://github.com/hashicorp/web-unified-docs)  ![GitHub Repo stars](https://img.shields.io/github/stars/hashicorp/web-unified-docs?style=social)

该项目是 HashiCorp 的统一产品文档仓库，旨在集中托管所有产品文档并逐步替代现有的 content API。核心功能包括：

1. **统一文档 API**：从 `/content` 目录加载并服务文档内容，支持多版本管理，作为 Dev Portal 的主要数据源之一。
2. **链接监控**：每周扫描生成破损链接报告并触发告警；PR 提交时自动检查并提示错误（仅信息提示，不阻断开发）。
3. **本地开发**：支持通过 Docker 和 Make 命令快速启动本地 API 和前端预览环境，便于功能测试。
4. **迁移工具**：提供脚本协助将旧仓库文档迁移至新中心，并在原位置自动添加迁移指引。
5. **架构整合**：新 API 与现有内容 API 共同向 Dev Portal 提供服务，实现从分散源码到统一源头的过渡。