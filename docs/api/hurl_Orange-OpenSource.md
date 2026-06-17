### [hurl](https://github.com/Orange-OpenSource/hurl) ![GitHub Repo stars](https://img.shields.io/github/stars/Orange-OpenSource/hurl?style=social)

Hurl 是一个用 Rust 编写的命令行工具，通过简单的纯文本格式定义和执行 HTTP 请求。

**核心功能**：
- 支持链式请求，可捕获响应值并在后续请求中复用（如 CSRF token）
- 支持多种请求类型：GET/POST/PUT/HEAD 等，支持表单数据、JSON、XML、GraphQL、SOAP
- 支持变量模板和动态数据生成

**测试功能**：
- 支持 JSONPath、XPath、状态码、响应头、Cookie 等断言
- 支持响应内容完整性校验（SHA-256）
- 支持 SSL 证书验证
- 支持性能测试（响应时间断言）
- 支持重试和轮询机制

**集成与输出**：
- 支持多种报告格式：HTML、JSON、JUnit、TAP
- 支持重定向控制、代理设置、Cookie 管理
- 支持 AWS Signature Version 4 签名
- 支持 HTTP/1.0、HTTP/1.1、HTTP/2、HTTP/3
- 底层基于 libcurl，单二进制文件易于安装