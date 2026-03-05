
---
title: grpc-gateway
---

### [grpc-ecosystem grpc-gateway](https://github.com/grpc-ecosystem/grpc-gateway)  ![GitHub Repo stars](https://img.shields.io/github/stars/grpc-ecosystem/grpc-gateway?style=social)

gRPC-Gateway 是一个 Protocol Buffers 编译器（protoc）插件，通过读取 protobuf 服务定义自动生成反向代理服务器，将 RESTful HTTP 请求转换为 gRPC 调用，使服务能同时提供 gRPC 和 HTTP/JSON 接口。

核心功能包括：
1. **HTTP 映射**：根据 `google.api.http` 注解将 gRPC 方法映射为 HTTP 端点，支持路径、查询和请求体参数。
2. **流式处理**：支持将 gRPC 流式 API 映射为 newline-delimited JSON 流。
3. **API 文档**：可选生成 OpenAPI (Swagger) v2 定义。
4. **元数据转换**：处理 HTTP 头信息（如授权、自定义头）与 gRPC 元数据的交互。
5. **灵活配置**：支持通过注解、默认规则或外部配置文件定制 HTTP 映射。