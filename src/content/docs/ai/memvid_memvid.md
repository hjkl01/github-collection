
---
title: memvid
---

### [memvid memvid](https://github.com/memvid/memvid)  ![GitHub Repo stars](https://img.shields.io/github/stars/memvid/memvid?style=social)

**项目核心内容总结：**

Memvid 是一个无需数据库的单文件 AI 内存系统，支持持久化、版本化和可移植的长期记忆管理，提供快速检索能力。其核心功能包括：  
- **智能帧结构**：以视频编码灵感为基础，将数据、嵌入向量、元数据封装为不可变的“智能帧”，实现高效压缩、索引和并行读取。  
- **特性**：支持时间旅行调试（回溯内存状态）、多模态数据处理（文本、音频、图像）、自动压缩升级、全文检索（BM25）和向量相似度搜索（HNSW）。  

**使用方法**：  
- **语言支持**：提供 Rust、Node.js、Python SDK 及 CLI 工具，Rust 依赖通过 `cargo add memvid-core` 安装，可按需启用搜索、向量、音频转录等功能。  
- **操作示例**：通过 API 创建内存文件、添加数据、执行搜索，支持多线程处理和加密胶囊（`.mv2e`）。  

**主要特性**：  
- 单文件存储（`.mv2`），无需额外数据库文件；  
- 支持跨会话分支、版本控制和数据回溯；  
- 适用场景包括企业知识库、离线 AI 系统、医疗/法律/金融领域代理等。  

**文件结构**：包含头信息、WAL 日志、压缩数据段、全文索引（Tantivy）、向量索引（HNSW）等模块，完整格式见 `MV2_SPEC.md`。  

**许可证**：Apache 2.0 开源协议。