
---
title: memvid
---

### [Olow304 memvid](https://github.com/Olow304/memvid)  ![GitHub Repo stars](https://img.shields.io/github/stars/Olow304/memvid?style=social)

Memvid 是一个面向 AI 代理的单文件内存层系统，无需依赖数据库即可提供持久、版本化且可移植的长期记忆。

*   **单文件架构**：所有数据、嵌入、索引及元数据封装在单个 `.mv2` 文件中，支持本地离线运行，无侧边文件。
*   **Smart Frames**：采用追加只写帧结构，支持时间旅行调试、崩溃安全及类视频编码的高效压缩。
*   **多模态处理**：原生支持文本、PDF、音频（Whisper）及图像（CLIP），提供本地 ONNX 或云端 OpenAI 嵌入。
*   **高性能检索**：具备超低延迟和高吞吐量，支持全文、向量及时序检索。
*   **跨语言支持**：提供 Rust、Python、Node.js SDK 及 CLI 工具，适用于 AI 代理、企业知识库及自动化工作流。