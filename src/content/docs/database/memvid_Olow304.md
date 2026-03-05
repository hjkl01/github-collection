
---
title: memvid
---

### [Olow304 memvid](https://github.com/Olow304/memvid)  ![GitHub Repo stars](https://img.shields.io/github/stars/Olow304/memvid?style=social)

Memvid 是一个为 AI 代理设计的单机记忆层，无需数据库或服务器即可实现持久化、版本化和便携化存储。其核心采用“智能帧”架构，将数据、索引和元数据封装在单个 `.mv2` 文件中，支持追加写入、高效压缩及时间线回溯。系统提供全模态检索能力（文本、向量、图像、音频），支持本地或云端嵌入，具有超低延迟和离线优先特性。提供 Rust 核心库及 Python、Node.js SDK 和 CLI 工具，适用于长期运行代理、知识库及工作流自动化。