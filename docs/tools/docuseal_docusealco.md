### [docuseal](https://github.com/docusealco/docuseal) ![GitHub Repo stars](https://img.shields.io/github/stars/docusealco/docuseal?style=social)

DocuSeal 是一个开源的文档填写与电子签署平台，提供安全高效的数字文档签署和处理能力。它支持通过可视化方式创建可填写的 PDF 表单，用户可在任意设备（含移动端）在线填写和签署。

核心功能包括：PDF 表单字段编辑（所见即所得）、12 种字段类型（签名、日期、文件、复选框等）、单文档多签署人、SMTP 自动邮件通知、自动 PDF 电子签名与签名验证、用户管理、多语言界面、API 与 Webhooks 集成，以及快速部署。文件可存储在本地磁盘或 AWS S3、Google Cloud Storage、Azure 等云存储中。

高级功能（Pro）包括：企业品牌定制与白标、用户角色、自动提醒、短信邀请与身份验证、条件字段与公式、CSV/XLSX 批量发送、SSO/SAML、通过 HTML/PDF/DOCX API 创建模板，以及 React/Vue/Angular/JavaScript 的嵌入式签署表单与表单构建器。

部署方面支持 Docker、Docker Compose，以及 Heroku、Railway、DigitalOcean、Render 等平台；默认使用 SQLite，也可通过 `DATABASE_URL` 切换到 PostgreSQL 或 MySQL。项目采用 AGPLv3（含附加条款）许可证。