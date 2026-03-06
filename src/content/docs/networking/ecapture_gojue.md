
---
title: ecapture
---

### [gojue ecapture](https://github.com/gojue/ecapture)  ![GitHub Repo stars](https://img.shields.io/github/stars/gojue/ecapture?style=social)

eCapture 是一款基于 eBPF 技术的 Linux 与 Android 系统监控工具，无需 CA 证书即可捕获 SSL/TLS 加密流量明文。主要功能如下：

1. **加密流量捕获**：支持 OpenSSL、LibreSSL、BoringSSL、GnuTLS、NSPR 等库，提供 Pcap、Keylog、Text 三种模式；支持 GoTLS 程序（Golang HTTPS/TLS）流量解密。
2. **主机安全审计**：支持 Bash 和 Zsh 命令捕获；支持 MySQL 和 PostgreSQL 数据库 SQL 查询审计。

项目支持 ELF 二进制文件和 Docker 运行，需 ROOT 权限，并配套提供 eCaptureQ 图形化客户端及 HTTP 远程配置功能。