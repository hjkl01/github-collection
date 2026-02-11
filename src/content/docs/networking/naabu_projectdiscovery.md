
---
title: naabu
---

### [projectdiscovery naabu](https://github.com/projectdiscovery/naabu)  ![GitHub Repo stars](https://img.shields.io/github/stars/projectdiscovery/naabu?style=social)

**项目功能：**  
Naabu 是一个用 Go 语言编写的高效端口扫描工具，支持快速可靠地枚举主机的有效端口。它支持 SYN/CONNECT/UDP 扫描，适用于单个主机或多个目标，输出支持 TXT、JSON 等格式，可与 Nmap 等工具集成进行服务探测。

**使用方法：**  
通过命令行调用，支持以下方式：
- 指定主机扫描：`naabu -host example.com`
- 指定端口扫描：`naabu -p 80,443`
- 从文件读取主机列表：`naabu -list hosts.txt`
- 支持 CIDR、ASN、IP 等多种输入方式
- 支持 UDP 扫描并可自定义数据包内容：`naabu -p u:53 -cp "DNS query payload"`
- 支持 IPv4 和 IPv6 扫描
- 支持 CDN/WAF 排除扫描（如 Cloudflare、Akamai 等）
- 支持主机发现（Host Discovery）功能
- 可与 Nmap 集成进行服务识别
- 支持配置文件设置默认参数
- 支持输出到文件或标准输出，可与 httpx 等工具管道结合使用

**主要特性：**
- 支持 SYN/CONNECT/UDP 扫描
- DNS 端口扫描与自动去重
- 支持 IPv4/IPv6（实验性）
- 支持被动扫描（通过 Shodan）
- 支持主机发现（ARP、ICMP、TCP 等方式）
- 支持多种输入格式（主机、IP、CIDR、ASN）
- 支持多种输出格式（JSON、TXT）
- 支持 CDN/WAF 排除扫描
- 支持 Nmap 集成进行服务识别
- 支持自定义 UDP 负载
- 支持配置文件设置默认参数
- 支持云平台（ProjectDiscovery Cloud）上传结果
- 支持以库的方式集成到 Go 项目中

**安装方式：**  
支持从 GitHub 下载二进制文件或通过 Docker 安装，也可使用 Go 安装：  
```sh
go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
```

**注意事项：**  
- 需安装 libpcap 库
- 建议以 root 用户运行以获得最佳性能
- 可调节速率、线程数等参数优化扫描效果