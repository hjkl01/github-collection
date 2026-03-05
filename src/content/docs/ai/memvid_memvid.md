
---
title: memvid
---

### [memvid memvid](https://github.com/memvid/memvid)  ![GitHub Repo stars](https://img.shields.io/github/stars/memvid/memvid?style=social)

Memvid 是专为 AI 代理设计的单文件记忆层系统，无需数据库即可实现持久化、版本化和便携式的长期记忆。

核心功能：
1. **单文件存储**：将数据、嵌入及索引封装为单个 .mv2 文件，支持离线本地检索，无需服务器。
2. **智能帧机制**：采用不可变追加式帧结构，支持时间轴追溯、高效压缩、崩溃恢复及版本管理。
3. **多模态检索**：支持全文搜索、向量相似性、视觉搜索、音频转录及本地或云端文本嵌入。
4. **高性能推理**：具备亚毫秒级检索延迟，支持多跳推理和时间逻辑。
5. **多语言 SDK**：提供 CLI 及 Rust、Node.js、Python 支持，模型无关且完全离线运行。

适用于长运行 AI 代理、企业知识库、离线系统、代码理解及审计型 AI 工作流等场景。