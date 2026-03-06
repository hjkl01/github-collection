
---
title: cosign
---

### [sigstore cosign](https://github.com/sigstore/cosign)  ![GitHub Repo stars](https://img.shields.io/github/stars/sigstore/cosign?style=social)

Cosign 是 Sigstore 项目下的工具，用于对 OCI 容器及其他工件进行签名和验证，旨在实现“隐形基础设施”。

主要功能包括：
1. **多种工件支持**：支持容器镜像、Blob、Tekton Bundles、WASM、eBPF 及 In-Toto 声明的签名、验证与存储。
2. **灵活签名机制**：
   - 默认支持基于 Fulcio CA 和 Rekor 透明日志的“无密钥签名”。
   - 支持硬件安全模块（HSM）、云 KMS、传统公私钥对及自有 PKI。
3. **广泛注册表兼容**：签名存储于 OCI 注册表，兼容 AWS、GCP、Azure、Docker Hub 等多种容器注册服务。
4. **离线验证**：支持在隔离环境中通过本地签名包进行验证。
5. **高级特性**：支持声明（Attestations）、签名计数器（Counter-signing）及标签签名。