
---
title: scan4all
---

### [hktalent scan4all](https://github.com/hktalent/scan4all)  ![GitHub Repo stars](https://img.shields.io/github/stars/hktalent/scan4all?style=social)

scan4all 是一款基于 Go 语言开发的跨平台一体化综合安全扫描工具（红队工具），集成了 vscan、nuclei、nmap、subfinder 等多种模块，主要功能包括：

1. **漏洞扫描**：支持 15000+ POC 检测（涵盖 CVE、CMS、中间件等），7000+ Web 指纹识别，146 种协议及 90000+ 规则端口扫描。
2. **密码爆破**：支持 RDP、SSH、MySQL、Redis、SMB 等 23 种服务的弱口令探测，支持自定义字典及 HTTP 密码智能爆破。
3. **子域名与安全检测**：具备 SSL 智能分析（自动子域名遍历）、蜜罐自动识别与跳过、供应链漏洞识别及 HTTP 请求走私检测。
4. **灵活扩展**：支持多种输入输出格式（JSON/CSV/Elasticsearch 等），可深度定制配置文件及扫描参数，高度适配 Linux、Windows 及 macOS 环境。