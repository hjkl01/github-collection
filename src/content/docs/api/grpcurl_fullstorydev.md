
---
title: grpcurl
---

### [fullstorydev grpcurl](https://github.com/fullstorydev/grpcurl)  ![GitHub Repo stars](https://img.shields.io/github/stars/fullstorydev/grpcurl?style=social)

grpcurl 是一个用于与 gRPC 服务器交互的命令行工具，功能类似于 curl 之于 HTTP。其核心功能包括：

1. **RPC 调用**：支持从命令行执行各类 RPC 方法（含双向流式传输），接受 JSON 格式请求体并自动转换为 Protobuf 二进制格式进行传输。
2. **服务探索**：支持通过服务器反射、Proto 源文件或 Protoset 文件列出服务名称及描述服务结构。
3. **连接支持**：支持 TLS 加密连接（含双向证书认证）及明文传输。
4. **库集成**：提供 Go 语言库包，便于开发者构建其他动态调用 gRPC 端点的工具。