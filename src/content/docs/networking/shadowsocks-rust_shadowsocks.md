
---
title: shadowsocks-rust
---

### [shadowsocks shadowsocks-rust](https://github.com/shadowsocks/shadowsocks-rust)  ![GitHub Repo stars](https://img.shields.io/github/stars/shadowsocks/shadowsocks-rust?style=social)

**项目核心内容总结：**  

**项目功能**  
Shadowsocks-rust 是一个基于 Rust 语言实现的 Shadowsocks 代理工具，支持 SOCKS5、HTTP/HTTPS 代理协议，提供加密传输、访问控制、负载均衡等功能，适用于科学上网及网络代理需求。  

**使用方法**  
通过配置文件定义服务器地址、加密方式、端口等参数，使用 `sslocal`（本地代理）、`ssserver`（远程服务器）、`ssmanager`（管理多用户）等命令行工具启动服务。支持插件扩展（如混淆插件），可通过 `ssurl` 工具生成或解析 Shadowsocks 链接。  

**主要特性**  
1. **加密算法**：支持 AEAD 2022 加密（如 `aes-256-gcm`）、流加密（如 `chacha20-ietf-poly1305`）及多种过时算法。  
2. **协议支持**：兼容 SOCKS5（含 UDP）、SOCKS4/4a、HTTP CONNECT 隧道协议。  
3. **高级功能**：  
   - 负载均衡与服务器延迟检测；  
   - ACL 访问控制（白名单/黑名单规则，支持正则表达式）；  
   - 插件系统（如混淆、HTTP 伪装）；  
   - 管理 API（支持多用户管理）。  
4. **其他**：防御重放攻击、支持 Windows 系统、MIT 许可证开源。  

**适用场景**  
适用于需要代理加密流量、绕过网络限制的用户，以及需自建代理服务器的开发者。