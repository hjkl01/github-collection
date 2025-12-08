
---
title: SafeLine
---

### [chaitin SafeLine](https://github.com/chaitin/SafeLine)

SafeLine 是一款自托管的 Web 应用防火墙（WAF），用于防御 SQL 注入、XSS、代码注入、路径遍历、暴力破解等常见攻击，支持动态加密 HTML/JS 代码、IP 限流、反爬虫挑战、访问控制等功能。  

**核心功能**：  
- 防御多种 Web 攻击（如 SQL 注入、XXE、SSRF 等）  
- 通过速率限制抵御 DoS 攻击和流量激增  
- 反爬虫验证（区分人类用户与机器人）  
- 访问认证挑战（强制输入密码访问）  
- 动态加密 HTML/JS 代码  

**使用方法**：  
- 安装：参考 [安装指南](https://docs.waf.chaitin.com/en/GetStarted/Deploy)  
- 配置：通过 [配置文档](https://docs.waf.chaitin.com/en/GetStarted/AddApplication) 添加保护的 Web 应用  

**特性亮点**：  
- 检测准确率高达 99.45%（优于 ModSecurity 和 CloudFlare）  
- 全球超 18 万次安装，保护超 100 万网站  
- 支持中文版文档及 Discord 社区支持  

**注意事项**：  
中国大陆用户安装国际版可能因云服务连接问题需参考中文文档。