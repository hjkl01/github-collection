
---
title: cloudflared
---

### [cloudflare cloudflared](https://github.com/cloudflare/cloudflared)  ![GitHub Repo stars](https://img.shields.io/github/stars/cloudflare/cloudflared?style=social)

该项目是 Cloudflare Tunnel 的命令行客户端 (`cloudflared`)，作为一个隧道守护进程，用于在 Cloudflare 网络与用户原始服务之间代理流量。其功能包括：无需在防火墙上开启端口即可安全暴露内部服务；支持通过隧道代理 TCP 流量（如 SSH、RDP）访问受保护的源头；提供多种安装部署方式（二进制、Docker、各平台包管理及源码构建）；支持创建隧道并配置流量路由（DNS、负载均衡器或 WARP 私有网络）；包含开发构建、测试及代码格式化等工具。