
---
title: caddy
---

### [caddyserver caddy](https://github.com/caddyserver/caddy)

**项目核心内容总结：**

**项目简介**  
Caddy 是一个基于 Go 语言开发的可扩展服务器平台，支持 HTTP/1.1、HTTP/2 和 HTTP/3，具备自动 HTTPS 功能，适用于各类 Web 服务场景。

**核心功能**  
1. **自动 HTTPS**：默认集成 ZeroSSL 和 Let's Encrypt，支持公共域名和内网证书管理，可集群协作。  
2. **灵活配置**：支持 Caddyfile、JSON、YAML 等多格式配置，提供动态 API 调整配置。  
3. **高性能与可扩展性**：支持百万级站点部署，模块化架构允许通过插件扩展功能（如数据库支持）。  
4. **跨平台兼容**：无需依赖外部库（如 libc），可在任意环境运行。  

**使用方法**  
- **安装**：从 [GitHub Releases](https://github.com/caddyserver/caddy/releases) 下载二进制文件，或通过 `xcaddy` 工具构建自定义版本（支持插件和版本信息）。  
- **开发构建**：需 Go 1.25+，执行 `git clone` 后使用 `go build` 编译，Linux 系统需通过 `setcap` 授权低权限端口绑定。  

**文档与支持**  
- 完整文档见 [https://caddyserver.com/docs/](https://caddyserver.com/docs/)，包含配置教程、API 参考等。  
- 社区支持通过 [Caddy 论坛](https://caddy.community) 获取，企业用户可联系 Ardan Labs 获取付费支持。  

**其他**  
- 项目名称“Caddy”为注册商标，应规范称呼为“Caddy”或“Caddy Web Server”。  
- 由 ZeroSSL（Stack Holdings 旗下）维护，Debian 包托管于 Cloudsmith。