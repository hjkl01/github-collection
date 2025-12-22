
---
title: check-if-email-exists
---

### [reacherhq check-if-email-exists](https://github.com/reacherhq/check-if-email-exists)  ![GitHub Repo stars](https://img.shields.io/github/stars/reacherhq/check-if-email-exists?style=social)

**项目核心内容总结：**  
`check-if-email-exists` 是一个开源工具，用于验证电子邮件地址是否存在，无需发送邮件。其功能包括：  
- **检查内容**：验证邮件可达性、语法合法性、DNS记录、SMTP服务器响应、邮箱是否被禁用、是否为临时邮箱、是否为角色账户等。  
- **使用方法**：  
  1. **Docker部署HTTP后端**：通过命令运行容器，发送POST请求验证邮件。  
  2. **CLI工具**：下载二进制文件，直接在本地运行验证。  
  3. **Rust库集成**：通过Cargo.toml引入库，在代码中调用API。  
- **特性**：支持代理配置、提供详细JSON输出（如邮件是否可达、SMTP连接状态等），并包含SaaS版本（[Reacher](https://reacher.email)）。  
- **许可证**：开源版本遵循AGPL-3.0，商业用途需购买商业许可证。  

**主要用途**：替代付费邮箱验证服务，适用于自建验证系统、数据清洗等场景。