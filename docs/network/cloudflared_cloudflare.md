### [cloudflare cloudflared](https://github.com/cloudflare/cloudflared)  ![GitHub Repo stars](https://img.shields.io/github/stars/cloudflare/cloudflared?style=social)

`cloudflared` 是 Cloudflare Tunnel 的命令行客户端，用于在 Cloudflare 网络与用户源站之间建立安全隧道。

**主要功能：**
*   **流量代理**：将 Cloudflare 流量转发至源站（如 Web 服务器），无需在防火墙上开放端口，确保源站安全。
*   **协议支持**：支持 HTTP/WebSocket 代理，以及 Layer 4 TCP 流量（如 SSH、RDP）的访问控制。
*   **灵活路由**：支持通过公共 DNS 记录、Cloudflare 负载均衡器或 WARP 私有网络将流量路由至隧道。
*   **多平台部署**：提供二进制文件、Docker 镜像及多种系统包，支持源码构建、测试与代码质量检查。

使用前需在 Cloudflare 仪表板添加网站并更改域名服务器。