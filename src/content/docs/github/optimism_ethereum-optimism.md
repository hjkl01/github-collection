
---
title: optimism
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/ethereum-optimism/optimism?style=social) ](https://github.com/ethereum-optimism/optimism)
### [ethereum-optimism optimism](https://github.com/ethereum-optimism/optimism)

**项目核心内容总结：**

Optimism 是一个以太坊扩展性解决方案，通过 OP Stack 技术栈构建可扩展的区块链（如 OP Mainnet 和 Base），旨在实现去中心化经济与治理系统。其核心特性包括：

1. **功能与架构**  
   - 提供 L2 区块链基础设施，支持高吞吐量交易处理与跨链互操作性。  
   - 核心组件包括：交易批处理（op-batcher）、节点客户端（op-node）、争议解决（op-challenger）、智能合约（contracts-bedrock）等，涵盖共识层、数据可用性、安全验证等模块。

2. **使用方法**  
   - 开发者可通过 [Optimism 文档](https://docs.optimism.io) 构建 dApp 或部署 OP Stack 区块链。  
   - 提供本地开发工具（如 devnet-sdk、op-devstack）和测试框架（op-e2e、op-acceptance-tests）支持链上测试。

3. **开发与协作**  
   - 采用开源模式，贡献流程详见 [CONTRIBUTING.md](./CONTRIBUTING.md)，鼓励社区参与。  
   - 主开发分支为 `develop`，合约变更需谨慎处理，避免向后不兼容。生产版本按 `<component-name>/v<semver>` 格式发布（如 `op-node/v1.1.2`），智能合约版本独立管理。

4. **安全与治理**  
   - 漏洞报告参考 [Security Policy](https://github.com/ethereum-optimism/.github/blob/master/SECURITY.md)，设有 Immunefi 赏金计划（最高 $200万）。  
   - 治理讨论在 [Optimism Governance Forum](https://gov.optimism.io/) 进行。

5. **许可证**  
   - 项目代码遵循 MIT 许可证。