
---
title: libsignal
---

### [signalapp libsignal](https://github.com/signalapp/libsignal)  ![GitHub Repo stars](https://img.shields.io/github/stars/signalapp/libsignal?style=social)

libsignal 是为 Signal 官方客户端和服务器提供平台无关 API 的加密库，底层基于 Rust，提供 Java、Swift 及 TypeScript 接口。主要功能包括：实现 Signal 协议（含 Double Ratchet 算法）、提供加密原语（如 AES-GCM）、支持设备间数据传输、SGX/HSM 远程证明、零知识群组与凭证、账户 PIN 密钥管理、用户名生成与验证以及媒体处理工具。该库仅限 Signal 内部使用，不支持外部集成。