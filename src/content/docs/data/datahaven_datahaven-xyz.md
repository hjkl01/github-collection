
---
title: datahaven
---

### [datahaven-xyz datahaven](https://github.com/datahaven-xyz/datahaven)  ![GitHub Repo stars](https://img.shields.io/github/stars/datahaven-xyz/datahaven?style=social)

**项目核心内容总结**  

**功能**  
DataHaven 是一个基于 EigenLayer 的去中心化存储平台，提供可验证的数据存储服务，适用于 AI 训练数据、机器学习模型、物联网数据及现实资产（RWA）等场景。支持跨链通信（Ethereum ↔ DataHaven），并通过 Merkle 证明确保数据完整性。  

**使用方法**  
1. **本地开发**：通过 Docker 构建镜像，使用 Kurtosis 启动测试网络；运行 E2E 测试验证功能。  
2. **开发流程**：修改智能合约或 Rust 代码后，需重新生成类型绑定（`bun generate:wagmi`/`bun generate:types`），并运行单元测试（`forge test`/`cargo test`）。  
3. **部署**：通过 GitHub Actions 自动化测试、构建 Docker 镜像并发布。  

**主要特性**  
- **可验证存储**：数据分片后生成 Merkle 树，通过链上根哈希验证完整性；BSP（备份节点）随机审计确保数据可用性。  
- **双层提供者网络**：MSP（主节点）负责数据读取，BSP（备份节点）保障冗余，违规节点将被链上惩罚。  
- **EigenLayer 安全**：验证者通过以太坊质押 ETH 获得经济保障，违规行为触发链上罚没。  
- **EVM 兼容**：支持 Solidity 合约部署及 Ethereum 工具链（如 MetaMask）。  
- **跨链通信**：基于 Snowbridge 实现资产与消息的无信任桥接，支持 BEEFY 共识证明。  

**适用场景**  
AI/ML 数据存储、物联网数据存证、现实资产（如产权记录）的链上存档。