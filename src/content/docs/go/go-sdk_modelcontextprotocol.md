
---
title: go-sdk
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/modelcontextprotocol/go-sdk?style=social) ](https://github.com/modelcontextprotocol/go-sdk)
### [modelcontextprotocol go-sdk](https://github.com/modelcontextprotocol/go-sdk)

**项目核心内容总结**  
MCP Go SDK 是 Model Context Protocol（MCP）的官方 Go 语言开发工具包，提供构建和使用 MCP 客户端与服务器的完整功能。  

**主要功能**  
- 通过 `mcp` 包实现 MCP 协议的核心 API，支持创建客户端/服务器实例、工具注册与调用。  
- `jsonrpc` 包用于自定义传输协议的实现。  
- `auth` 和 `oauthex` 包提供 OAuth 认证及扩展功能（如 ProtectedResourceMetadata）。  
- 完整兼容 MCP 规范，文档与代码示例位于 `docs/` 和 `examples/` 目录。  

**使用方法**  
- **服务器端**：创建 `mcp.Server` 实例，添加工具并绑定传输（如 stdin/stdout），运行服务。  
- **客户端**：通过 `mcp.Client` 连接服务器，调用工具并处理响应。  
- 示例代码包含基于 stdin/stdout 的简单工具（如 `SayHi`）及客户端调用逻辑。  

**特性**  
- 提供开箱即用的 `StdioTransport` 和 `CommandTransport` 传输方式。  
- 支持 OAuth 认证扩展，适配多种 MCP 场景。  
- 包含完整示例（`examples/`）和详细文档（`docs/`）。  

**其他**  
- 开源 MIT 协议，兼容第三方 Go MCP SDK（如 mcp-go）。