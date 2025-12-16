
---
title: inbucket
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/inbucket/inbucket?style=social) ](https://github.com/inbucket/inbucket)
### [inbucket inbucket](https://github.com/inbucket/inbucket)

**项目核心内容总结：**  
Inbucket 是一个用于测试电子邮件的工具，能够接收任意邮箱地址的邮件，并通过网页、REST API 和 POP3 接口提供访问。其核心特性包括：  
1. **无外部依赖**：内置 HTTP、SMTP、POP3 服务及存储功能，编译后无需额外依赖。  
2. **多协议支持**：提供 REST API（含 Go 客户端库）及 POP3 接口，支持邮件管理。  
3. **快速部署**：支持 Docker 镜像一键启动（`latest` 和 `edge` 标签），或通过 Go 和 Node.js 从源码构建。  
4. **配置灵活**：默认配置可直接使用，亦可通过环境变量或配置工具自定义设置。  
5. **生产级稳定性**：已用于实际生产环境，提供版本更新日志及开源贡献指南。  

**使用方法**：  
- **Docker 启动**：运行 `docker run` 命令，映射端口后通过浏览器访问 `localhost:9000`。  
- **源码构建**：需安装 Go 和 Node.js，执行 `git clone`、`yarn build` 和 `go build` 流程后启动服务。