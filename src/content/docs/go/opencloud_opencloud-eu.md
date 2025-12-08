
---
title: opencloud
---

### [opencloud-eu opencloud](https://github.com/opencloud-eu/opencloud)

**核心内容总结：**  
OpenCloud 是一个基于 Go 语言开发的开源服务器后端项目，提供云服务相关功能。项目使用 Apache 2.0 许可证，支持通过 OpenID Connect 认证（兼容 Keycloak 等外部 IdP 或内置 LibreGraph Connect 服务），数据存储于文件系统（默认路径为 `$HOME/.opencloud/`）。  

**使用方法：**  
1. 生成资源文件：`make generate`  
2. 编译二进制文件：`make -C opencloud build`  
3. 启动服务：`opencloud/bin/opencloud init && opencloud/bin/opencloud server`  

**主要特性：**  
- 无数据库依赖，采用文件系统存储数据；  
- 支持灵活的用户认证方式；  
- 提供本地测试环境快速部署能力。