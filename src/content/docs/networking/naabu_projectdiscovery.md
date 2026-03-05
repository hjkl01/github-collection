
---
title: naabu
---

### [projectdiscovery naabu](https://github.com/projectdiscovery/naabu)  ![GitHub Repo stars](https://img.shields.io/github/stars/projectdiscovery/naabu?style=social)

Naabu 是一款用 Go 编写的快速端口扫描工具，用于高效枚举主机的有效端口。它支持 SYN、CONNECT 和 UDP 扫描，具备 DNS 端口扫描、IPv4/IPv6 支持、基于 Shodan 的被动端口枚举及主机发现功能。工具支持集成 Nmap 进行服务发现，可排除 CDN/WAF 地址，支持自定义 UDP 负载。兼容多种输入源（如主机、IP、CIDR、ASN）和输出格式（JSON、TXT 等），既可作为命令行工具使用，也可作为库集成，并提供配置化支持及扫描指标监控。