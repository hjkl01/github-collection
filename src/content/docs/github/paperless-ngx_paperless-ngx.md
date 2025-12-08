
---
title: paperless-ngx
---

### [paperless-ngx paperless-ngx](https://github.com/paperless-ngx/paperless-ngx)

**Paperless-ngx 核心内容总结：**

1. **项目功能**  
   Paperless-ngx 是一款文档管理工具，可将纸质文件数字化为可搜索的在线档案，帮助用户减少纸质文件使用。支持文档扫描、存储、检索及管理，兼容从旧版 Paperless-ng 迁移。

2. **使用方法**  
   - 推荐通过 Docker Compose 部署，项目提供安装脚本快速配置环境。  
   - 安装命令：`bash -c "$(curl -L https://raw.githubusercontent.com/paperless-ngx/paperless-ngx/main/install-paperless-ngx.sh)"`  
   - 详细步骤见官方文档。

3. **主要特性**  
   - 多语言支持（通过 Crowdin 协作翻译）。  
   - 社区驱动开发，支持功能讨论、问题反馈及贡献代码。  
   - 提供在线演示环境（需注意数据非持久化）。  
   - 文档齐全，包含功能说明、截图及部署指南。

4. **安全注意事项**  
   - **禁止在不可信主机上运行**，因数据以明文存储且无加密。  
   - 建议部署于本地服务器，并配置备份以保障安全。