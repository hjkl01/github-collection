
---
title: vault
---

### [hashicorp vault](https://github.com/hashicorp/vault)  ![GitHub Repo stars](https://img.shields.io/github/stars/hashicorp/vault?style=social)

Vault 是一个用于安全访问密钥的工具，为 API 密钥、密码、证书等敏感信息提供统一的访问接口、严格的访问控制及详细审计日志。核心功能包括：

1. **安全密钥存储**：加密存储任意键值对，防止通过原始存储窃取数据。
2. **动态密钥**：按需生成特定系统（如 AWS、SQL）的凭证，并在租赁到期后自动撤销。
3. **数据加密**：提供数据加密和解密服务，无需存储数据本身，允许开发者委托加密管理。
4. **租赁与续期**：为每个密钥关联租赁期，到期自动撤销，支持客户端续期。
5. **密钥撤销**：支持撤销单个或批量密钥（如特定用户或类型），辅助密钥轮换及系统入侵防御。