
---
title: optimism
---

### [ethereum-optimism optimism](https://github.com/ethereum-optimism/optimism)  ![GitHub Repo stars](https://img.shields.io/github/stars/ethereum-optimism/optimism?style=social)

本项目是 Optimism 核心代码仓库，包含构建 OP Stack 去中心化软件栈所需的核心组件，旨在扩展以太坊技术并支撑 OP Mainnet 和 Base 等区块链网络。

核心功能包括：
1. Rollup 核心组件：提供 rollup 共识层客户端（op-node）、L2 批量提交器（op-batcher）和 L2 输出提交器（op-proposer）。
2. 智能合约：包含 OP Stack 基础智能合约（contracts-bedrock）。
3. 安全与证明：集成链上 MIPS 模拟器（cannon）、故障证明程序（op-program）及争议游戏挑战代理（op-challenger）。
4. 运维工具：涵盖部署管理（op-deployer）、高可用 sequencing 服务（op-conductor）及各类测试、监控工具。

项目遵循“影响=利润”原则，提供完整的文档与规范，支持开发者构建和扩展基于 OP Stack 的区块链。