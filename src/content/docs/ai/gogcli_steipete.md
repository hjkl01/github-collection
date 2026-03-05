
---
title: gogcli
---

### [steipete gogcli](https://github.com/steipete/gogcli)  ![GitHub Repo stars](https://img.shields.io/github/stars/steipete/gogcli?style=social)

gogcli 是一款运行于终端的高效命令行工具，用于直接操作 Google Workspace 各项服务。其主要功能总结如下：

1. **多服务支持**：涵盖 Gmail、Calendar、Drive、Docs、Slides、Sheets、Forms、Classroom、Chat、Contacts、Tasks、People、Groups 及 Keep 等 Google 核心服务。
2. **脚本友好**：默认提供 JSON 格式输出，便于自动化脚本处理、数据解析及与其他工具管道连接。
3. **安全认证与存储**：支持 OAuth2 授权及 Workspace 服务账号（域内委托），使用系统密钥环或加密文件安全存储凭证，支持最小权限授权（Least-privilege auth）。
4. **多账户管理**：支持同时管理多个 Google 账户（支持别名设置），可隔离不同 OAuth 客户端配置。
5. **高级特性**：包含邮件阅读追踪、Gmail 事件监听（Pub/Sub 推送）、文档 sed 风格编辑（sedmat）、批量操作等功能。
6. **交互体验**：支持人类可读的表格输出、Shell 自动补全、多模式颜色控制及本地时区处理。