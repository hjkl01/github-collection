
---
title: vault
---

### [hashicorp vault](https://github.com/hashicorp/vault)  ![GitHub Repo stars](https://img.shields.io/github/stars/hashicorp/vault?style=social)

Vault 是一款用于安全访问和管理机密的工具，提供统一的接口及详细的审计日志。其核心功能包括：

1. **安全密钥存储**：加密存储任意键值对，支持多种持久化后端。
2. **动态密钥生成**：按需生成（如 AWS、数据库），到期自动撤销。
3. **数据加密服务**：提供加密解密功能，无需开发者自行设计加密方案。
4. **租约管理**：为密钥关联租约，支持续期，到期自动撤销。
5. **灵活撤销**：支持撤销单个密钥、密钥树或特定类型密钥，便于密钥轮换及入侵响应。