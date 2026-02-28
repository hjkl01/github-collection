
---
title: cloud-mail
---

### [maillab cloud-mail](https://github.com/maillab/cloud-mail)  ![GitHub Repo stars](https://img.shields.io/github/stars/maillab/cloud-mail?style=social)

Cloud Mail 是一个基于 Cloudflare 平台的简约响应式邮箱服务。

**核心功能**：
- 支持邮件发送（集成 Resend，含附件、图片、群发及状态查看）。
- 支持邮件接收与转发（可转发至 TG 机器人或其他邮箱）。
- 支持附件收发（使用 R2 对象存储保存和下载）。
- 提供管理员功能（用户/邮件管理、RBAC 权限控制、资源限制）。
- 开放 API（支持批量生成用户、多条件查询邮件）。
- 数据可视化（使用 ECharts 展示系统数据及用户增长）。
- 支持个性化设置（自定义标题、背景、透明度）及 Turnstile 人机验证。

**部署与使用**：
- 仅需一个域名，部署至 Cloudflare Workers 即可创建多个邮箱。
- 响应式布局，自动适配 PC 和大部分手机端浏览器。
- 通过 Cloudflare 平台大幅降低服务器成本。

**技术栈**：
- 平台：Cloudflare Workers
- 后端：Hono、Drizzle、D1、KV、R2
- 前端：Vue3、Element Plus、ECharts
- 邮件服务：Resend
- 许可证：MIT