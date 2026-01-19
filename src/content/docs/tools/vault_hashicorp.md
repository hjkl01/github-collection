
---
title: vault
---

### [hashicorp vault](https://github.com/hashicorp/vault)  ![GitHub Repo stars](https://img.shields.io/github/stars/hashicorp/vault?style=social)

**项目核心内容总结：**  
Vault 是 HashiCorp 开发的工具，用于安全存储和管理敏感信息（如 API 密钥、密码、证书等）。其核心功能包括：  
1. **安全存储**：加密存储数据，防止未授权访问；  
2. **动态生成秘密**：按需生成临时密钥（如 AWS 或数据库凭证），使用后自动失效；  
3. **数据加密**：支持对数据进行加密和解密，无需自行设计加密方案；  
4. **租约与续期**：为每个秘密设置租约，到期自动撤销，支持手动续期；  
5. **撤销控制**：可批量撤销特定用户或类型的秘密，用于密钥轮换或应急锁定。  

**使用方法**：  
- 开发需安装 Go，克隆仓库后运行 `make bootstrap` 初始化环境；  
- 使用 `make dev` 构建项目，`make test` 运行测试；  
- 接受测试（Acceptance Test）需注意可能涉及真实资源（如云服务账户），需提前配置环境变量；  
- 提供 Docker 测试支持，可通过自定义镜像和集群配置进行集成测试。