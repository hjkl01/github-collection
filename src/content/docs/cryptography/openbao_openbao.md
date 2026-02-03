
---
title: openbao
---

### [openbao openbao](https://github.com/openbao/openbao)  ![GitHub Repo stars](https://img.shields.io/github/stars/openbao/openbao?style=social)

OpenBao 是一个用于管理、存储和分发敏感数据（如密钥、证书和秘密）的开源软件。其目标是提供一个基于开放治理原则的社区驱动的解决方案，适用于现代系统对多种秘密的管理需求。OpenBao 支持安全存储、动态生成秘密、数据加密、租约与续期、以及撤销机制等功能。

### 核心功能：
- **安全秘密存储**：支持任意键值对的加密存储，数据写入持久化存储前会进行加密。
- **动态秘密生成**：可按需为系统（如 AWS、SQL 数据库）生成临时凭证，并在租约到期后自动撤销。
- **数据加密**：可加密和解密数据，无需存储密文，便于安全团队统一管理加密策略。
- **租约与续期**：所有秘密都有租约，到期后自动撤销，客户端可通过 API 续期。
- **撤销机制**：支持单个秘密或一组秘密的撤销，有助于密钥轮换和入侵后的系统锁定。

### 使用方法：
- **开发环境搭建**：需要安装 Go，推荐将项目克隆到 GOPATH 之外，并运行 `make bootstrap` 初始化环境。
- **编译开发版本**：运行 `make dev` 或 `make static-dist dev-ui` 生成可执行文件。
- **运行测试**：使用 `make test` 运行单元测试，`make testacc` 运行集成测试。
- **Docker 测试**：支持通过 Docker 容器运行测试，适用于本地开发和集成测试。

### 文档与社区：
- 官网：[https://www.openbao.org](https://www.openbao.org)
- 文档：[https://www.openbao.org/docs/](https://www.openbao.org/docs/)
- 邮件列表、GitHub 讨论区、Zulip 聊天服务器等社区资源齐全，支持开发与协作。