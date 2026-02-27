
---
title: himalaya
---

### [pimalaya himalaya](https://github.com/pimalaya/himalaya)  ![GitHub Repo stars](https://img.shields.io/github/stars/pimalaya/himalaya?style=social)

**项目名称**：Himalaya  
**项目类型**：命令行电子邮件管理工具（CLI）

---

### 核心功能

- 多账户支持，支持交互式向导或手动 TOML 配置文件设置账户
- 支持多种后端：
  - IMAP
  - Maildir
  - Notmuch
  - SMTP
  - Sendmail
- 支持通过系统全局密钥环管理密码（keyring）
- 支持 OAuth 2.0 授权流程
- 支持 PGP 加密（通过命令、GPG 或原生实现）
- 支持 JSON 格式输出
- 基于编辑器（$EDITOR）撰写邮件
- 支持多个邮件服务商配置模板（如 Gmail、Proton Mail、Outlook、iCloud 等）
- 提供丰富的调试选项（--debug、--trace、环境变量控制日志等级）

---

### 使用方法

- **安装方式**：
  - 通过 `install.sh` 脚本安装
  - 通过 Cargo 安装（支持自定义功能模块）
  - 通过包管理器安装（Arch、Homebrew、Scoop、Fedora、Nix 等）
  - 从源码构建

- **配置方式**：
  - 使用向导交互式配置账户
  - 手动编辑 TOML 配置文件

- **邮件操作命令示例**：
  - `himalaya envelope list --account posteo --folder Archives.FOSS --page 2`

---

### 主要特性

- 支持多种邮件服务商的自动配置
- 支持邮件附件和 MML 语法撰写邮件
- 支持命令行接口（CLI）与 TUI 工具集成（如 Vim、Emacs 插件）
- 支持国际化认证（OAuth 2.0）和加密（PGP）
- 提供调试和日志输出功能（通过环境变量控制）
- 项目基于 Rust 编写，模块化设计，支持 Cargo 特性开关

---

### 其他

- 社区支持：Matrix、Mastodon
- 可通过多种方式赞助支持该项目（GitHub Sponsors、Ko-fi、Buy Me a Coffee 等）