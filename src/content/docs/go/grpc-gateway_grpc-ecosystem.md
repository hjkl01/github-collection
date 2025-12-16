
---
title: grpc-gateway
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/grpc-ecosystem/grpc-gateway?style=social) ](https://github.com/grpc-ecosystem/grpc-gateway)
### [grpc-ecosystem grpc-gateway](https://github.com/grpc-ecosystem/grpc-gateway)

### 项目核心内容总结

**项目功能**：  
该项目是一个 gRPC 到 HTTP 的网关工具，用于将 gRPC 服务暴露为 RESTful API，支持生成 JSON API 处理器、反向代理、OpenAPI 文档等。

**使用方法**：  
可以通过 `buf` 或 `protoc` 工具进行代码生成。使用 `buf` 可以管理插件版本，使用 `protoc` 需要配置插件参数。支持通过注解、外部配置文件等方式定义 HTTP 映射规则。

**主要特性**：  
- 支持将 gRPC 接口转换为 RESTful API；
- 支持查询参数、路径参数、请求体等方法参数；
- 支持枚举、流式接口、HTTP 头映射到 gRPC 元数据；
- 可生成 OpenAPI v2 文档；
- 支持 PATCH 请求转换为 Field Mask；
- 支持 Protobuf Editions（2023 版）和 Go Opaque API；
- 可配置 JSON 序列化方式，支持自定义路径模板。

**其他信息**：  
- 项目使用 BSD 3-Clause 许可证；
- 提供了丰富的示例和文档，包括视频教程；
- 不支持 XML 编码、双向流式通信等特性。