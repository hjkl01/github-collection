
---
title: cloudflared
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/cloudflare/cloudflared?style=social) ](https://github.com/cloudflare/cloudflared)
### [cloudflare cloudflared](https://github.com/cloudflare/cloudflared)

**核心内容总结：**  
该项目是Cloudflare Tunnel的命令行客户端，用于将Cloudflare网络流量安全代理至用户本地服务器，无需开放防火墙端口。主要功能包括：通过隧道实现HTTP/HTTPS流量转发，支持Layer 4 TCP协议（如SSH、RDP）的私有网络访问，以及通过WARP客户端访问隧道后端服务。  

**使用方法：**  
1. 在Cloudflare控制台添加网站并配置域名解析；  
2. 通过多种方式安装`cloudflared`（如Homebrew、Docker、Linux包等）；  
3. 创建隧道并配置DNS记录、负载均衡器或WARP客户端实现流量路由；  
4. 支持通过`cloudflared tunnel`和`cloudflared access`命令管理隧道及访问控制。  

**主要特性：**  
- 支持无需公网IP的内网服务暴露；  
- 提供TryCloudflare测试环境；  
- 版本支持范围限制在最新版本一年内；  
- 开发者可使用Go语言构建及测试工具链进行本地开发。