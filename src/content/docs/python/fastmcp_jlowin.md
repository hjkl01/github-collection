
---
title: fastmcp
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/jlowin/fastmcp?style=social) ](https://github.com/jlowin/fastmcp)
### [jlowin fastmcp](https://github.com/jlowin/fastmcp)

**项目核心内容总结：**  
FastMCP 是一个用于构建和部署 MCP（模型通信协议）服务的 Python 工具包，支持多种传输协议（STDIO、HTTP、SSE）和企业级认证（OAuth、JWT、API Key 等）。主要功能包括：  
1. **快速开发**：通过 `FastMCP.run()` 一键启动本地服务器，支持工具（tool）、资源（resource）定义及客户端调用。  
2. **企业级安全**：内置 Google、GitHub、Azure 等主流 OAuth 提供商，支持零配置认证，客户端可自动完成浏览器授权流程。  
3. **灵活部署**：支持本地运行、FastMCP 云服务（HTTPS、认证、免配置）及自托管（HTTP/SSE）。  
4. **高级特性**：支持代理服务器、多服务器组合、OpenAPI/FastAPI 集成，可生成符合 MCP 规范的接口。  
5. **测试与调试**：提供内存内客户端测试、自动化测试套件及代码质量检查（prek）。  

**使用方法**：  
- 本地运行：`fastmcp run server.py`  
- 客户端连接：通过 `Client` 对象调用工具或资源，支持多种传输方式（如 HTTP/SSE）。  
- 认证配置：通过 `auth=XXX` 参数启用 OAuth/JWT 等认证机制。