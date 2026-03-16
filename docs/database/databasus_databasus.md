### [databasus databasus](https://github.com/databasus/databasus)  ![GitHub Repo stars](https://img.shields.io/github/stars/databasus/databasus?style=social)

Databasus 是一款免费、开源、自托管的数据库备份工具，核心支持 PostgreSQL，同时兼容 MySQL、MariaDB 和 MongoDB。主要功能如下：

- **灵活调度**：支持小时、日、周、月或 Cron 表达式等定时任务，具备智能压缩能力。
- **保留策略**：提供基于时间、数量或 GFS（祖父子）模式的保留策略，支持设置存储容量限制。
- **多端存储**：支持本地存储及 S3、Google Drive、NAS、SFTP 等多种云存储，备份文件支持独立加密解密，避免厂商锁定。
- **通知服务**：支持通过邮件、Slack、Telegram、Discord 等渠道发送备份进度通知。
- **安全加密**：采用 AES-256-GCM 加密，默认使用只读用户连接，敏感数据全程加密保护。
- **团队协作**：支持工作区分组、基于角色的权限管理（RBAC）及操作审计日志。
- **部署与界面**：基于 Docker 或 Kubernetes 部署，提供美观的响应式 Web 管理界面，支持暗/亮色主题。