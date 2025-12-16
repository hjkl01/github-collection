
---
title: certbot
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/certbot/certbot?style=social) ](https://github.com/certbot/certbot)
### [certbot certbot](https://github.com/certbot/certbot)

**核心内容总结：**  
Certbot 是由 EFF 开发的工具，用于自动化获取和部署 Let's Encrypt 提供的 SSL/TLS 证书，帮助用户轻松启用和管理 HTTPS。  

**功能与使用方法：**  
- **适用场景**：支持 Apache、Nginx 等主流 Web 服务器，也支持通过 Webroot 或 Standalone 模式验证域名控制权。  
- **操作方式**：需在服务器上直接运行，通常需要管理员权限。用户可通过 [交互指南](https://certbot.eff.org) 获取定制化指令。  
- **证书管理**：自动生成私钥（支持 ECDSA 和 RSA），可与 Let's Encrypt 或其他 ACME 兼容服务交互，支持证书撤销和自动 HTTPS 重定向。  

**主要特性：**  
- 全流程自动化，减少人工干预；  
- 支持多种服务器及第三方插件扩展；  
- 私钥本地生成，保障安全性；  
- 配置变更可记录并回退。  

**贡献与协作**：  
开发者可参考 [贡献指南](https://certbot.eff.org/docs/contributing.html) 参与项目，需遵守 EFF 的代码规范。  

**相关链接**：  
- 官方文档：[https://certbot.eff.org/docs](https://certbot.eff.org/docs)  
- GitHub 项目：[https://github.com/certbot/certbot](https://github.com/certbot/certbot)  
- Let's Encrypt 官网：[https://letsencrypt.org](https://letsencrypt.org)