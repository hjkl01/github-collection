
---
title: fizzy
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/basecamp/fizzy?style=social) ](https://github.com/basecamp/fizzy)
### [basecamp fizzy](https://github.com/basecamp/fizzy)

**项目核心内容总结：**

Fizzy 是 37signals 开发的看板工具，用于跟踪问题和想法。其核心功能包括任务管理、邮件通知、Web 推送通知等。

**使用方法：**
1. **部署**  
   - 通过 [Kamal](https://kamal-deploy.org/) 部署到自有服务器，需配置 `config/deploy.yml` 文件，设置服务器地址、SSL、SMTP 邮件参数等。  
   - 环境变量（如密钥、SMTP 账号密码）需存放在 `.kamal/secrets` 文件中，不可提交到版本库。  
   - 部署命令：首次运行 `bin/kamal setup`，后续使用 `bin/kamal deploy`。

2. **开发**  
   - 安装依赖并运行 `bin/setup` 初始化环境，`bin/dev` 启动本地开发服务器（访问地址：http://fizzy.localhost:3006）。  
   - 生成 VAPID 密钥以支持 Web 推送通知，通过 `bin/rails c` 中的 `WebPush.generate_key` 生成。  
   - 数据库支持 SQLite 和 MySQL，通过 `DATABASE_ADAPTER` 环境变量切换。

**主要特性：**
- **文件存储**：默认使用本地磁盘，支持通过 `ACTIVE_STORAGE_SERVICE` 配置为 S3 等云存储。  
- **邮件系统**：支持 SMTP 配置，开发环境可通过 `letter_opener` 预览邮件。  
- **测试**：提供单元测试（`bin/rails test`）和完整 CI 测试（`bin/ci`）。  
- **SaaS 支持**：集成 `fizzy-saas` 模块，适配 37signals 的计费系统（需内部私有仓库依赖）。  

**许可证**：采用 [O'Saasy License](LICENSE.md) 开源协议。