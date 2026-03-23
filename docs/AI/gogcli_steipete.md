### [steipete gogcli](https://github.com/steipete/gogcli)  ![GitHub Repo stars](https://img.shields.io/github/stars/steipete/gogcli?style=social)

gogcli 是一款快速、脚本友好的终端命令行工具，用于在本地直接管理 Google 各类服务及 Google Workspace 功能。

核心功能：
1. **服务覆盖**：支持 Gmail（邮件搜索/收发/追踪）、Calendar（事件/冲突/团队日程）、Drive（文件管理/权限/转换）、Docs/Slides/Sheets（编辑/导出/Markdown 处理）、Classroom（教学管理）、Chat、Tasks、Forms、Contacts、Apps Script 及 Keep 等。
2. **脚本友好**：提供 JSON 首选输出模式，支持人类可读及纯文本格式，便于自动化集成。
3. **多账号管理**：支持同时管理多个 Google 账号及别名，可自动选择默认或特定账号。
4. **安全认证**：使用系统密钥环或加密文件存储 OAuth 令牌，支持最小权限授权（只读/特定范围），兼容 Workspace 服务账户（域内委派）。
5. **特色功能**：包含邮件打开追踪、文档 Sedmat 风格编辑、本地时间显示、Shell 自动补全及命令白名单沙箱控制。