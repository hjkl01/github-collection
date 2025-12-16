
---
title: helix-db
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/HelixDB/helix-db?style=social) ](https://github.com/HelixDB/helix-db)
### [HelixDB helix-db](https://github.com/HelixDB/helix-db)

**核心内容总结：**

HelixDB 是一个用 Rust 构建的开源图向量数据库，支持图+向量数据模型，也可处理 KV、文档和关系数据。其核心功能包括：  
- **内置工具**：支持 MCP（数据发现与图遍历）、自动文本向量化（无需预处理）、RAG 应用所需向量搜索、关键词搜索和图遍历。  
- **安全与性能**：默认私有化访问，通过编译后的 HelixQL 查询访问数据；基于 LMDB 存储引擎，实现超低延迟。  
- **开发特性**：100% 类型安全的 HelixQL 查询语言，确保生产环境查询可靠性。  

**使用方法**：  
1. 安装 CLI 工具（`curl` 命令）；  
2. 初始化项目并编写 `.hx` 文件定义数据结构与查询；  
3. 通过 `helix check` 验证查询，`helix push dev` 部署到 API；  
4. 使用 TypeScript/Python SDK 调用接口（默认端口 6969）。  

**许可证**：AGPL 协议；提供商业托管服务（需联系 `founders@helix-db.com`）。