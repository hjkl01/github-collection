
---
title: grpc-gateway
---

### [grpc-ecosystem grpc-gateway](https://github.com/grpc-ecosystem/grpc-gateway)  ![GitHub Repo stars](https://img.shields.io/github/stars/grpc-ecosystem/grpc-gateway?style=social)

gRPC-Gateway 是基于 Protobuf 编译器 protoc 的插件，用于生成反向代理服务器。它根据服务定义中的 HTTP 注解或外部配置，将 RESTful HTTP 请求转换为 gRPC 调用，实现服务同时提供 gRPC 和 HTTP/JSON 接口。

主要功能：
- 自动生成 gRPC 服务存根、HTTP 网关代理代码及 OpenAPI 定义。
- 支持 HTTP 路径、请求体、查询参数映射至 gRPC 方法，自动处理 JSON 与 Protobuf 转换。
- 支持流式响应、超时控制、Header 元数据传递及 PATCH 转 Field Mask。
- 支持通过 Go Modules 或远程插件进行工具依赖管理和构建集成。

暂不支持：HTTP 头参数、Trailer 元数据、XML 编码及双向流。