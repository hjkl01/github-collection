
---
title: SafeLine
---

### [chaitin SafeLine](https://github.com/chaitin/SafeLine)  ![GitHub Repo stars](https://img.shields.io/github/stars/chaitin/SafeLine?style=social)

SafeLine 是一款自托管的 Web 应用防火墙（WAF），通过反向代理模式部署在 Web 应用前端，用于过滤、监控和阻断恶意 HTTP/S 流量以保护应用安全。其核心功能包括：

- **防御 Web 攻击**：拦截 SQL 注入、XSS、代码注入、命令注入、RCE、XXE、SSRF、路径遍历、后门等多种威胁。
- **速率限制**：基于 IP 进行流量节流，防御 DoS 攻击、暴力破解及流量滥用。
- **反机器人挑战**：通过人机验证机制区分人类用户与恶意爬虫。
- **身份验证挑战**：启用后可强制访客输入密码，否则拦截访问。
- **动态保护**：动态加密 Web 服务器中的 HTML 和 JS 代码。
- **访问控制列表**：支持基于 IP 的 Web 访问控制管理。