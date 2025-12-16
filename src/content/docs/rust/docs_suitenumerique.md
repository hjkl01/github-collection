
---
title: docs
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/suitenumerique/docs?style=social) ](https://github.com/suitenumerique/docs)
### [suitenumerique docs](https://github.com/suitenumerique/docs)

### 核心内容总结  
**项目功能**：Docs 是一个协作文本编辑器，支持实时协作、内容安全控制、多格式导出（如 `.docx`、`.pdf`）及子页面知识管理，适用于团队知识共建与共享。  

**使用方法**：  
- 浏览器测试：访问提供的[演示文档链接](https://impress-preprod.beta.numerique.gouv.fr/docs/6ee5aac4-4fb9-457d-95bf-bb56c2467713/)。  
- 本地运行：需安装 Docker 和 Docker Compose，通过 `make bootstrap` 初始化项目，使用默认账号 `username: impress`、`password: impress` 登录。  

**主要特性**：  
- **写作**：支持 Markdown 语法、多种区块类型、离线编辑、AI 辅助功能（如改写、翻译）。  
- **协作**：实时编辑、权限控制、多格式导出。  
- **自托管**：支持 Kubernetes、Docker Compose 等部署方式，社区提供多种安装方案。  
- **许可证**：核心代码为 MIT，部分高级功能依赖 GPL 许可证的组件，可通过环境变量 `PUBLISH_AS_MIT` 排除。  

**其他**：项目由法国与德国政府联合开发，使用 Django、Next.js、BlockNote.js 等技术栈，支持多语言翻译及社区贡献。