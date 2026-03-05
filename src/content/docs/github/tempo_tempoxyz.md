
---
title: tempo
---

### [tempoxyz tempo](https://github.com/tempoxyz/tempo)  ![GitHub Repo stars](https://img.shields.io/github/stars/tempoxyz/tempo?style=social)

Tempo 是一个专为大规模稳定币支付设计的区块链网络，核心功能如下：

1. **支付专用架构**：基于 TIP-20 代币标准，提供专用支付通道以避免网络拥堵，内置合规策略及链上对账功能。
2. **低成本稳定币费用**：Gas 费支持以稳定币支付，通过 Fee AMM 自动转换，单笔转账成本低于 0.001 美元。
3. **智能账户功能**：支持原子批量支付、费用代付、定时支付及 Passkeys（生物识别）认证。
4. **高性能与 EVM 兼容**：基于 Reth SDK 和 Simplex 共识实现亚秒级最终性；完全兼容以太坊虚拟机及工具链（Solidity、Foundry 等）。
5. **开发者支持**：提供 TypeScript、Rust、Go 等 SDK，支持本地节点运行及公共测试网接入，适用于金融及支付基础设施。