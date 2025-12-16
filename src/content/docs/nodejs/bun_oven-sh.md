
---
title: bun
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/oven-sh/bun?style=social) ](https://github.com/oven-sh/bun)
### [oven-sh bun](https://github.com/oven-sh/bun)

**核心内容总结：**  
Bun 是一个高性能的 JavaScript/TypeScript 运行时环境，提供丰富的内置工具和功能，适用于开发、测试和部署。  

**主要功能：**  
1. **文件操作**：支持文件读写、删除、路径转换、压缩/解压（gzip/DEFLATE）等。  
2. **网络与通信**：内置 HTTP/HTTPS 服务器、WebSocket 服务（支持发布-订阅、压缩）、HTTP 客户端。  
3. **数据处理**：支持 JSON、Blob、字符串、Base64 编码解码、UUID 生成、密码哈希、正则表达式等。  
4. **测试工具**：提供单元测试、快照测试、Mock 函数、代码覆盖率分析、浏览器 DOM 测试等。  
5. **流处理**：支持 ReadableStream/Node.js 流与 Buffer、String、ArrayBuffer 等格式的互转。  
6. **实用工具**：包含睡眠、时间设置、环境变量管理、路径解析、执行 shell 命令等功能。  

**使用方法：**  
通过命令行或 API 调用 Bun 提供的模块，如 `bun test` 运行测试、`bun build` 构建项目，或使用内置函数（如 `Bun.write()`、`Bun.sleep()`）直接操作。  

**主要特性：**  
- 高性能，内置 V8 引擎优化；  
- 无需额外依赖，集成常用工具（如 HTTP 服务器、测试框架）；  
- 支持与 Node.js 兼容的 API，降低迁移成本；  
- 提供丰富的调试和分析工具（如内存快照、代码覆盖率）。