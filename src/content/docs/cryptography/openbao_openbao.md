
---
title: openbao
---

### [openbao openbao](https://github.com/openbao/openbao)  ![GitHub Repo stars](https://img.shields.io/github/stars/openbao/openbao?style=social)

OpenBao 是一个开源软件，用于管理、存储和分发敏感数据（如密钥、证书和凭证）。其核心功能包括：安全秘密存储（加密保存密钥/值对，支持多种后端）、动态秘密（按需生成临时凭证并自动撤销）、数据加密（提供加密解密服务而不存储数据）、租赁机制（所有秘密均具有租约，支持自动过期和续约）以及秘密撤销（支持撤销单个或批量秘密）。项目基于 Go 语言开发，提供 API 和 SDK 供其他项目集成。