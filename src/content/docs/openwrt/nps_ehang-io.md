---
title: nps
---

### [ehang-io nps](https://github.com/ehang-io/nps)
### [ ![GitHub Repo stars](https://img.shields.io/github/stars/ehang-io/nps?style=social) ](https://github.com/ehang-io/nps)

**项目核心内容总结：**

**功能**  
NPS 是一款轻量级、高性能的内网穿透代理服务器，提供 Web 管理界面，支持 TCP/UDP/HTTP(S)/SOCKS5 等协议，可实现跨平台（Linux、Windows、macOS 等）的内网穿透。支持 HTTPS 集成、流量/带宽限制、域名解析自定义、多用户管理等功能。

**使用方法**  
1. **安装**：下载对应系统的服务器包，解压后执行安装命令（Linux/macOS 使用 `sudo ./nps install`，Windows 以管理员身份运行 `nps.exe install`）。  
2. **启动**：通过 `sudo nps start`（Linux/macOS）或 `nps.exe start`（Windows）启动服务，默认 Web 管理端口为 8080。  
3. **配置**：访问 Web 界面（默认账号密码：admin/123），创建客户端并复制命令执行连接。  
4. **管理**：通过 Web 界面配置穿透服务、监控流量及系统信息。

**主要特性**  
- 兼容主流协议及多平台，支持系统服务注册。  
- 提供 Web 管理界面，支持 HTTPS、自定义域名解析、流量控制等。  
- 支持多用户及客户端版本管理，可查看实时带宽、流量等信息。  
- 扩展功能包括缓存、加密、端口复用等。
