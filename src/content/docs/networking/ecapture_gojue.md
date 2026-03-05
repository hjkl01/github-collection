
---
title: ecapture
---

### [gojue ecapture](https://github.com/gojue/ecapture)  ![GitHub Repo stars](https://img.shields.io/github/stars/gojue/ecapture?style=social)

eCapture 是一款基于 eBPF 技术的工具，无需 CA 证书即可在 Linux/Android 系统（需 ROOT 权限）下捕获 SSL/TLS 明文内容。

核心功能包括：
1. **加密库明文捕获**：支持 OpenSSL、GnuTLS、NSS、BoringSSL 等库，提供 Pcap（保存明文包）、Keylog（保存主密钥）、Text（直接输出明文）三种模式。
2. **GoTLS 捕获**：支持 Golang 程序加密通信（HTTPS/TLS）的明文捕获。
3. **主机安全审计**：支持 Bash、Zsh 命令捕获，以及 MySQL、PostgreSQL 的 SQL 查询审计。

工具支持 ELF 二进制文件与 Docker 部署，提供 HTTP 接口用于动态配置更新及事件转发。