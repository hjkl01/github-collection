
---
title: hyperswitch
---

### [juspay hyperswitch](https://github.com/juspay/hyperswitch)  ![GitHub Repo stars](https://img.shields.io/github/stars/juspay/hyperswitch?style=social)

Hyperswitch 是一个基于 Rust 构建的可组合开源支付基础设施，被誉为“支付领域的 Linux"。它采用模块化架构，允许企业按需集成支付组件，无需供应商锁定。核心功能包括：

- **成本可观测性**：监控、审计并优化支付成本。
- **收入恢复**：通过智能重试策略减少被动流失。
- **Vault**：提供 PCI 合规的支付凭证安全存储。
- **智能路由**：自动将交易路由至授权率最高的支付服务提供商（PSP）。
- **自动化对账**：支持双向及三向对账。
- **多种支付方式**：支持卡片、数字钱包（Apple Pay 等）及 BNPL 等全球支付方式。

项目支持 Docker 本地快速部署、托管沙箱环境测试以及 AWS、GCP、Azure 等云原生部署，旨在为开发者提供灵活、可控且高可靠性的支付栈解决方案。