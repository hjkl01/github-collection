
---
title: scan4all
---

### [hktalent scan4all](https://github.com/hktalent/scan4all)  ![GitHub Repo stars](https://img.shields.io/github/stars/hktalent/scan4all?style=social)

scan4all 是一款基于 Go 语言开发的跨平台轻量级综合漏洞扫描工具，专为红队测试设计。

1.  **漏洞检测**：集成 Nuclei、Vscan 等引擎，支持 15000+ 漏洞 POC（含 CVE、RCE、XSS 等）。
2.  **密码爆破**：支持 23 种协议（SSH、RDP、Redis、SMB 等）的弱口令及字典爆破。
3.  **端口扫描**：集成 Nmap 和 Naabu，支持 146 种协议及 90000+ 规则，支持自定义端口扫描。
4.  **指纹识别**：支持 7000+ Web 指纹识别及敏感文件探测。
5.  **资产分析**：包含智能 SSL 分析、子域名遍历及多 IP 关联扫描。
6.  **结果管理**：支持多种输入输出格式（JSON, CSV 等），可配置存储至 Elasticsearch。
7.  **高级特性**：支持 HTTP 请求走私检测、蜜罐自动识别及高度自定义配置。
8.  **兼容性**：开源轻量，支持 Linux、Windows、macOS 等多平台。