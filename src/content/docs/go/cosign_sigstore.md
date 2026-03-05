
---
title: cosign
---

### [sigstore cosign](https://github.com/sigstore/cosign)  ![GitHub Repo stars](https://img.shields.io/github/stars/sigstore/cosign?style=social)

Cosign 是 Sigstore 项目下的工具，用于对 OCI 容器及其他工件进行签名、验证和存储。

核心功能：
1. **签名方式灵活**：默认支持基于 Fulcio 和 Rekor 的“无密钥签名”，也支持硬件/KMS 及自定义密钥对签名。
2. **支持多种工件**：涵盖容器镜像、Blob、WASM、eBPF、Tekton Bundles 及 in-toto 证明等。
3. **存储与验证**：签名存储于 OCI 注册表，支持在线及离线环境下的验证。
4. **广泛兼容**：支持主流容器注册表。