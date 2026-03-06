
---
title: libsignal
---

### [signalapp libsignal](https://github.com/signalapp/libsignal)  ![GitHub Repo stars](https://img.shields.io/github/stars/signalapp/libsignal?style=social)

libsignal 是 Signal 官方客户端和服务器的平台无关通信协议库，底层使用 Rust 实现，封装为 Java、Swift 和 TypeScript 库。核心功能涵盖：实现 Signal 协议（含双棘轮算法）、加密原语、设备间传输、远程验证（SGX/HSM）、零知识群组与凭证、账户密钥管理（PIN）、用户名处理及媒体工具。该仓库专供 Signal 内部使用，不支持外部项目集成，采用 GNU AGPLv3 协议。