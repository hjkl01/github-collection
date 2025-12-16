
---
title: cosmos-sdk
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/cosmos/cosmos-sdk?style=social) ](https://github.com/cosmos/cosmos-sdk)
### [cosmos cosmos-sdk](https://github.com/cosmos/cosmos-sdk)

**Cosmos SDK 核心内容总结**  

**项目功能**  
Cosmos SDK 是一个模块化、开源的区块链开发框架，用于构建安全、高性能且高度可定制的 Layer 1 链，支持 200+ 生产级区块链。开发者可通过预置模块（如治理、权限管理、代币化等）或自定义模块快速搭建区块链，并通过 IBC 协议实现跨链互操作性。  

**主要特性**  
- **模块化架构**：支持功能模块灵活组合，涵盖账户管理、状态存储、治理等核心功能。  
- **原生互操作性**：内置 IBC 协议，实现跨链数据与资产传输。  
- **高性能共识**：推荐使用 CometBFT（原 Tendermint）作为共识引擎，支持高吞吐量与可配置性。  
- **开发者友好**：提供教程与示例代码，支持快速构建应用（如通过 `gaia` 框架）。  

**使用方法**  
1. 通过 [教程](https://tutorials.cosmos.network) 学习 SDK 基础与开发流程。  
2. 使用最新 Go 版本构建应用，参考 [文档](https://docs.cosmos.network/) 获取模块实现细节。  
3. 可基于 `gaia`（Cosmos Hub 的参考实现）进行二次开发。  

**维护与支持**  
由 Cosmos Labs（Interchain Foundation 子公司）维护，社区活跃，提供 Discord、Telegram 等技术支持渠道。