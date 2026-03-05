
---
title: Acontext
---

### [memodb-io Acontext](https://github.com/memodb-io/Acontext)  ![GitHub Repo stars](https://img.shields.io/github/stars/memodb-io/Acontext?style=social)

Acontext 是一个开源的代理技能记忆层，自动将代理运行中的经验（任务执行与结果）存储为可编辑的 Markdown 文件。与传统记忆方案不同，它记录“代理做了什么及结果”，而非仅存储对话或静态文档，旨在生成可复用的 SOP 和偏好设置。

核心功能：
1. **技能即文件**：知识以 Markdown 存储，支持 Git 管理，无 API 锁定，兼容多框架。
2. **自动化提炼**：从会话和工具调用中自动蒸馏有效操作和失败教训。
3. **工具化检索**：代理通过工具调用获取完整技能单元，依赖推理而非向量搜索。
4. **多端支持**：提供 Python 和 TypeScript SDK，支持云端及本地 Docker 部署。

适用于希望避免代理重复错误并自动化沉淀最佳实践的开发者。