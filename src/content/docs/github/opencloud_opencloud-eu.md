
---
title: opencloud
---

### [opencloud-eu opencloud](https://github.com/opencloud-eu/opencloud)

**项目核心内容总结：**

**功能**  
OpenCloud 服务器后端基于 Go 语言开发，提供核心服务功能，支持通过 OpenID Connect 认证（兼容 Keycloak 等外部 IdP 或内置 LibreGraph Connect 服务），数据存储依赖文件系统（默认路径为 `$HOME/.opencloud/`）。

**使用方法**  
1. 生成资源文件：`make generate`  
2. 编译二进制文件：`make -C opencloud build`  
3. 初始化并启动服务：  
   ```bash  
   opencloud/bin/opencloud init && opencloud/bin/opencloud server  
   ```  

**主要特性**  
- 无数据库设计，采用文件系统存储数据  
- 支持多种身份认证方式（OpenID Connect + 多种 IdP 选项）  
- 开源（Apache 2.0 许可证）并鼓励社区协作（文档编写、代码提交、问题反馈等）