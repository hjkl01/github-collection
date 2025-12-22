
---
title: evilginx2
---

### [kgretzky evilginx2](https://github.com/kgretzky/evilginx2)  ![GitHub Repo stars](https://img.shields.io/github/stars/kgretzky/evilginx2?style=social)

**项目核心内容总结：**

**功能**  
Evilginx 3.0 是一款基于 Go 语言开发的中间人攻击框架，用于钓鱼获取用户登录凭证及会话 Cookie，可绕过双因素认证保护。其通过自建 HTTP/DNS 服务器实现代理功能，无需依赖第三方工具，部署便捷。

**使用方法**  
需通过官方文档（[https://help.evilginx.com](https://help.evilginx.com)）安装配置，支持自动化服务器部署及 SQLite 数据库管理。

**主要特性**  
1. **技术实现**：完全用 Go 编写，集成独立 HTTP/DNS 服务器，无需依赖 Nginx。  
2. **高级功能**：  
   - 钓鱼检测规避（如绕过 Chrome 高级保护）  
   - 官方维护的钓鱼模板数据库  
   - Botguard 防止机器人流量  
   - Evilpuppet 模块（针对 Google 高级钓鱼）  
   - 支持多域名、通配符 TLS 证书及网站伪装  
3. **扩展支持**：  
   - 与 Gophish 集成（需使用特定版本）  
   - 提供付费版本 Evilginx Pro（含自动化部署、JavaScript/HTML 混淆等功能）  
4. **学习资源**：配套推出《Evilginx Mastery》培训课程，讲解反向代理钓鱼技术及 MFA 绕过方法。  

**限制**  
作者明确声明工具仅限合法渗透测试使用，禁止用于非法钓鱼活动。