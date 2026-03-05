
---
title: openbao
---

### [openbao openbao](https://github.com/openbao/openbao)  ![GitHub Repo stars](https://img.shields.io/github/stars/openbao/openbao?style=social)

OpenBao 是一个开源软件解决方案，用于管理、存储和分发敏感数据（包括密钥、证书和凭据）。其核心功能包括：
- 安全秘密存储：加密存储任意密钥值，防止底层存储泄露。
- 动态秘密生成：按需生成临时凭证，租约到期后自动撤销。
- 数据加密：提供加密和解密服务，无需应用层自行实现加密逻辑。
- 租约与续期：所有秘密均关联租约，支持自动过期撤销及 API 续期。
- 秘密撤销：支持撤销单个或树状结构的秘密，便于密钥轮换及安全响应。