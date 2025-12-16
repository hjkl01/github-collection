
---
title: grpc-go
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/grpc/grpc-go?style=social) ](https://github.com/grpc/grpc-go)
### [grpc grpc-go](https://github.com/grpc/grpc-go)

**项目核心内容总结：**  

1. **项目功能**  
   gRPC-Go 是 gRPC 的 Go 语言实现，提供高性能、开源的 RPC 框架，支持移动端和 HTTP/2 协议。  

2. **使用方法**  
   - 在代码中导入 `import "google.golang.org/grpc"`，通过 `go build` 等命令自动获取依赖。  
   - 中国用户需通过 `go mod replace` 替换依赖地址（如 `github.com/grpc/grpc-go@latest`）。  

3. **主要特性**  
   - 支持 HTTP/2 和移动端优化。  
   - 提供性能基准测试、示例代码、技术文档及贡献指南。  
   - 支持通过环境变量（如 `GRPC_GO_LOG_VERBOSITY_LEVEL`）控制日志输出。  

4. **常见问题**  
   - 连接关闭错误（`Unavailable`）可能由服务器配置、网络中断或 Keepalive 参数导致，需检查双方日志并调整参数（如 `MaxConnectionAgeGrace`）。  
   - 编译错误时需更新至最新版本（`go get google.golang.org/grpc`）。