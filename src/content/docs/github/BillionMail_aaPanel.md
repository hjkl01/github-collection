
---
title: BillionMail
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/aaPanel/BillionMail?style=social) ](https://github.com/aaPanel/BillionMail)
### [aaPanel BillionMail](https://github.com/aaPanel/BillionMail)

**核心内容总结：**  
BillionMail 是一个开源的邮件服务器和电子邮件营销平台，支持企业及个人管理邮件活动，提供高级分析、客户管理、无限发送、可定制模板、隐私保护及自托管功能。  

**使用方法：**  
1. **安装方式**：  
   - 一键安装（aaPanel）：通过 aaPanel 网站下载并安装。  
   - Docker 安装：克隆仓库后执行 `docker compose up -d`。  
   - 传统安装：运行 `bash install.sh` 脚本。  
2. **操作步骤**：安装后需连接域名、验证 DNS 记录、启用 SSL，然后创建邮件活动（选择邮件内容、联系人列表、发送时间等）。  

**主要特性：**  
- 完全开源，无隐藏费用。  
- 支持无限量邮件发送，无限制。  
- 提供邮件送达率、打开率等数据分析。  
- 自托管，数据私有，无第三方追踪。  
- 集成 RoundCube 邮件客户端（通过 `/roundcube/` 访问）。  

**其他：**  
- 提供演示环境（地址及默认账号密码）。  
- 支持通过管理脚本（如 `bm help`）查看配置、更新版本等。