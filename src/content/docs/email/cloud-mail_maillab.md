
---
title: cloud-mail
---

### [maillab cloud-mail](https://github.com/maillab/cloud-mail)  ![GitHub Repo stars](https://img.shields.io/github/stars/maillab/cloud-mail?style=social)

Cloud Mail 是基于 Cloudflare 的简约响应式邮箱服务，支持单域名创建多个邮箱。主要功能如下：

1. **低成本部署**：基于 Cloudflare Workers 生态（Workers/D1/R2/KV）部署，降低服务器成本。
2. **邮件收发**：集成 Resend 发送邮件（支持群发、内嵌图片及附件），使用 R2 对象存储处理附件收发。
3. **管理功能**：支持管理员对用户和邮件进行管理，具备 RBAC 权限控制及资源限制功能。
4. **邮件推送**：接收邮件后可转发至 Telegram 机器人或其他服务商邮箱。
5. **开放 API**：支持使用 API 批量生成用户及多条件查询邮件。
6. **数据可视化**：使用 ECharts 展示系统数据详情及用户邮件增长情况。
7. **个性化与安全**：支持自定义网站标题、背景等样式，集成 Turnstile 人机验证，界面响应式适配 PC 及移动端。