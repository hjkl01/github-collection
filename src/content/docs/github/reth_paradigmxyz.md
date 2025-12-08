
---
title: reth
---

### [paradigmxyz reth](https://github.com/paradigmxyz/reth)

**Reth核心内容总结：**

Reth是Paradigm开发的Ethereum全节点实现，采用Rust语言，具备模块化、高性能和社区驱动特性。支持连接Ethereum网络、交易处理、智能合约交互，兼容多种共识层（CL）实现及EVM链（如Optimism、Polygon等）。主要特性包括：

1. **模块化设计**：所有组件均可作为库使用，支持灵活组合与扩展。
2. **高性能**：基于Rust和Erigon的分阶段同步架构，结合优化后的Alloy和revm库。
3. **开源与许可证**：采用Apache/MIT双许可证，无商业限制。
4. **客户端多样性**：增强Ethereum网络抗脆弱性，避免单实现风险。
5. **多链支持**：支持Ethereum及主流EVM链的全同步。
6. **可配置性**：提供不同配置方案，适应不同硬件和使用场景（如快速查询、轻量级运行）。

**使用方法**：  
- 安装：通过[官方安装指南](https://paradigmxyz.github.io/reth/installation/installation.html)获取。  
- 运行：参考[用户文档](https://reth.rs)启动节点。  
- 开发者可直接使用其库（如[crate文档](https://reth.rs/docs)），或参与[Telegram社区](https://t.me/paradigm_reth)贡献代码。

**注意事项**：  
- 自v0.2.0-beta.1起，数据库格式有重大变更，旧版本需执行`reth db drop`后重新同步。  
- 审计信息：通过Sigma Prime和Guido Vranken的代码审计。  
- 开发者测试需安装Geth并运行`cargo nextest run`。