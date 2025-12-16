
---
title: grpcurl
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/fullstorydev/grpcurl?style=social) ](https://github.com/fullstorydev/grpcurl)
### [fullstorydev grpcurl](https://github.com/fullstorydev/grpcurl)

**核心内容总结：**  
`grpcurl` 是一个用于与 gRPC 服务器交互的命令行工具，功能类似于 `curl`，但专为 gRPC 设计。它支持通过 JSON 格式发送请求，自动转换为二进制 Protobuf 数据，便于人类和脚本使用。主要功能包括：  
1. **调用 RPC 方法**：支持所有类型（包括流式）的 RPC 调用，可通过 `-d` 参数发送 JSON 请求体，或通过标准输入（`-d @`）动态输入数据。  
2. **服务与方法浏览**：通过 `list` 命令列出服务器提供的服务及方法，支持使用服务器反射、Proto 源文件或预编译的 Protoset 文件解析服务定义。  
3. **描述符支持**：若服务器不支持反射，可通过 `-import-path` 指定 Proto 源文件路径，或使用 `-protoset` 指定 Protoset 文件获取服务定义。  

**主要特性**：  
- 支持 TLS/非 TLS 服务器及双向认证（mTLS）。  
- 支持交互式操作双向流式 RPC（通过终端输入输出）。  
- 提供库（`github.com/fullstorydev/grpcurl`）供开发其他动态调用 gRPC 的工具。  

**使用方法**：  
- **安装**：可通过 Homebrew、Docker、Snap 或 Go 安装（`go install`）。  
- **调用示例**：`grpcurl [参数] 服务器地址 方法路径`，如 `grpcurl -d '{"id":123}' grpc.server.com:443 my.service/Method`。  
- **高级功能**：使用 `describe` 查看服务定义详情，通过 `-H` 添加请求头，或用 `-protoset`/`-import-path` 指定描述符来源。