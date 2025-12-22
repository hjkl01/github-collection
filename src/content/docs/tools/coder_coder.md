
---
title: coder
---

### [coder coder](https://github.com/coder/coder)  ![GitHub Repo stars](https://img.shields.io/github/stars/coder/coder?style=social)

**项目核心内容总结：**  
Coder 是一个自托管的云开发环境工具，允许组织通过 Terraform 定义开发环境（如 EC2、Kubernetes Pod、Docker 容器等），并通过安全的 Wireguard 隧道连接，空闲时自动关闭资源以节省成本。  

**使用方法：**  
1. 通过安装脚本（`curl -L https://coder.com/install.sh | sh`）快速安装。  
2. 运行 `coder server` 启动服务，访问 `http://localhost:3000` 创建用户并配置工作区。  
3. 生产环境需指定 PostgreSQL 数据库和外部访问地址。  

**主要特性：**  
- 支持 Terraform 定义云资源，灵活适配多种云平台。  
- 自动关闭闲置资源，降低运维成本。  
- 集成 VS Code、JetBrains 等主流 IDE，支持 Dev Container 构建。  
- 提供模板、工作区管理、权限控制等完整开发环境管理功能。  
- 社区支持丰富，包含 GitHub Action、Terraform 部署方案等扩展工具。