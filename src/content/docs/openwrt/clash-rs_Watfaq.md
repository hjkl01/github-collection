
---
title: clash-rs
---

### [Watfaq clash-rs](https://github.com/Watfaq/clash-rs)  ![GitHub Repo stars](https://img.shields.io/github/stars/Watfaq/clash-rs?style=social)

ClashRS 是一款基于规则的网络代理软件，支持灵活的流量路由、多种代理协议及本地 DNS 服务。主要功能包括：  
- **流量规则**：根据 IP/域名/GeoIP 等条件实现精细化路由；  
- **DNS 服务**：提供本地防欺骗 DNS，支持 UDP/TCP/DoH/DoT 协议；  
- **代理模式**：可作为 HTTP/Socks5 代理或 utun 设备运行；  
- **协议支持**：兼容 Shadowsocks/Trojan/Vmess/Wireguard/Tor 等多种出站协议；  
- **动态配置**：支持远程加载规则和代理配置；  
- **追踪功能**：集成 Jaeger 进行性能追踪。  

**使用方法**：  
1. **安装**：通过预编译二进制、Docker 镜像或本地构建（需 cmake、libclang 等依赖）；  
2. **配置**：创建 YAML 配置文件（如 `port: 7890`）；  
3. **运行**：执行 `./clash -c config.yaml` 启动。  

**环境支持**：Linux、macOS、Windows（需手动添加 wintun.dll）及 iOS（需通过 App Store 或 TestFlight 安装）。