
---
title: gogcli
---

### [steipete gogcli](https://github.com/steipete/gogcli)  ![GitHub Repo stars](https://img.shields.io/github/stars/steipete/gogcli?style=social)

gogcli 是一个功能强大的命令行工具，允许用户在终端中操作 Google 的各种服务，如 Gmail、日历、文档、表格等。以下是其核心内容总结：

---

### 项目功能
gogcli 提供对 Google 服务的全面支持，包括：
- **Gmail**：搜索邮件、发送邮件、管理标签、过滤器等。
- **日历**：创建、更新事件，查看日程，检测冲突。
- **Google Classroom**：管理课程、学生、作业。
- **Google Chat**：创建空间、发送消息（仅限企业版）。
- **Google Drive**：上传、下载文件，管理权限。
- **Google Sheets / Docs / Slides**：读写文档、表格、演示文稿。
- **Google Tasks**：管理任务列表。
- **Google Contacts**：搜索、创建联系人。
- **Google Keep（仅限企业版）**：管理便签。
- **Google Groups**：管理群组成员（企业版）。
- **其他功能**：支持多账户、脚本自动化、安全认证、服务账户等。

---

### 使用方法
1. **安装**：支持 Homebrew、Arch Linux 和源码编译。
2. **配置 OAuth2 凭据**：需从 Google Cloud Console 获取并配置。
3. **添加账户**：通过 `gog auth add` 命令进行授权。
4. **使用命令**：通过 `gog [服务] [操作]` 的方式操作 Google 服务，如：
   - `gog gmail search "from:me"`
   - `gog calendar events --today`
   - `gog drive upload ./file.txt`

---

### 主要特性
- **多账户支持**：可同时管理多个 Google 账户。
- **脚本友好**：提供 JSON 格式输出，便于脚本自动化。
- **安全认证**：支持 OAuth2 和企业服务账户（Service Account）。
- **自动刷新令牌**：一次认证，长期使用。
- **最小权限认证**：支持只读模式，减少权限风险。
- **支持企业功能**：如 Google Workspace 的群组管理、Keep 等。
- **输出格式多样**：支持文本、JSON、TSV 等格式。
- **命令限制**：可设置命令白名单，用于沙箱环境。

---

### 安装方式
- **Homebrew**：`brew install steipete/tap/gogcli`
- **Arch Linux**：`yay -S gogcli`
- **源码编译**：克隆仓库并执行 `make`。

---

### 示例命令
- `gog gmail search 'newer_than:7d'`
- `gog calendar create primary --summary "Meeting" --from 2025-01-15T10:00:00Z --to 2025-01-15T11:00:00Z`
- `gog drive upload ./report.docx`

---

### 安全与配置
- **凭据存储**：默认使用系统密钥链，支持加密文件存储。
- **配置文件**：支持自定义时区、账户别名、默认输出格式等。
- **环境变量**：可设置默认账户、输出格式、时区等。

---

### 适用场景
- 自动化脚本：批量处理邮件、文档、日程等。
- 多账户管理：管理个人和企业 Google 账户。
- 企业集成：支持 Google Workspace 功能，如群组、服务账户等。

---

总结：gogcli 是一个全面的 Google 服务命令行工具，支持广泛功能，适合开发者和高级用户进行自动化管理和多账户操作。