
---
title: wstunnel
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/erebe/wstunnel?style=social) ](https://github.com/erebe/wstunnel)
### [erebe wstunnel](https://github.com/erebe/wstunnel)

**项目核心内容总结：**  
wstunnel 是一个基于 WebSocket 和 HTTP/2 协议的隧道工具，支持 TCP/UDP 流量转发、端口代理、反向隧道和透明代理等功能，适用于网络穿透、隐私保护等场景。  

**主要功能：**  
1. **协议支持**：通过 WebSocket（wss://）或 HTTP/2（https://）建立隧道，兼容防火墙限制。  
2. **安全特性**：支持 TLS 加密、自定义路径前缀（`--http-upgrade-path-prefix`）验证、证书自定义（如 Let's Encrypt）以避免指纹识别。  
3. **灵活配置**：可设置端口转发（-L）、反向隧道（-R）、透明代理（tproxy）、DNS 路由等，适配多种网络环境。  
4. **高性能**：支持大流量传输，通过调整 MTU、超时参数等优化吞吐量。  

**使用方法：**  
- **服务器端**：启动隧道服务，指定监听地址（如 `wss://[::]:443`），配置安全参数（如路径前缀、证书）。  
- **客户端**：连接服务器，设置转发规则（如 `-L socks5://127.0.0.1:8888`）或反向隧道（`-R tcp://[::]:8000:localhost:8000`）。  
- **高级用法**：结合透明代理工具（如 cproxy）实现全局流量代理，或通过反向隧道暴露本地服务到公网。  

**主要特性：**  
- 支持 UDP 流量（如 WireGuard 隧道）；  
- 可通过配置文件（`--restrict-config`）定义复杂访问规则；  
- 适配移动端（如 Termux 在 Android 上运行）；  
- 提供反向隧道和透明代理方案，实现本地服务远程访问和网络流量劫持防护。