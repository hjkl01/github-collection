
---
title: vaultwarden
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/dani-garcia/vaultwarden?style=social) ](https://github.com/dani-garcia/vaultwarden)
### [dani-garcia vaultwarden](https://github.com/dani-garcia/vaultwarden)

**核心内容总结：**  
Vaultwarden 是一个用 Rust 编写的 Bitwarden 客户端 API 替代服务器，适用于自托管部署，提供以下功能：  
- **功能**：支持个人密码保险库、文件传输、网站图标管理、多因素认证、组织管理（如团队协作、权限控制）、数据备份与恢复等，兼容官方 Bitwarden 客户端。  
- **使用方法**：推荐通过 Docker 或 Podman 安装，提供命令行和 Docker Compose 配置示例，需设置域名、持久化存储路径及反向代理；也可自行编译或使用社区维护的第三方包。  
- **特性**：轻量高效，支持反向代理部署，社区活跃，提供详细 Wiki 文档。  

**注意事项**：  
- 项目与 Bitwarden 公司无关联，由前员工独立维护；  
- 使用需自行负责数据安全，建议定期备份；  
- 曾用名 Bitwarden_RS，现更名以避免混淆。