
---
title: reth
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/paradigmxyz/reth?style=social) ](https://github.com/paradigmxyz/reth)
### [paradigmxyz reth](https://github.com/paradigmxyz/reth)

**项目核心内容总结：**  

**功能**  
Reth 是一个基于 Rust 的 Ethereum 全节点实现，支持连接 Ethereum 网络、处理交易、日志、追踪，以及与智能合约交互。作为 Execution Layer（EL），兼容所有支持 Engine API 的 Consensus Layer（CL）实现，可同步 Ethereum 及其他 EVM 链（如 Optimism、Polygon 等）。  

**使用方法**  
提供安装指南（[链接](https://paradigmxyz.github.io/reth/installation/installation.html)），用户可通过命令行运行节点。开发者可使用其库（如 Alloy、revm）进行二次开发，或参考 [开发者文档](./docs) 和 [ Crate 文档](https://reth.rs/docs/)。  

**主要特性**  
1. **模块化设计**：所有组件均作为库提供，支持灵活组合与扩展。  
2. **高性能**：基于 Rust 和 Erigon 的分阶段同步架构，结合优化后的 Ethereum 库（如 revm）。  
3. **开源与许可证**：采用 Apache/MIT 双许可证，无商业限制。  
4. **兼容性**：支持多种 EVM 链，数据库兼容性自 Beta.1 版本后无重大变更。  
5. **可配置性**：提供不同配置方案，适配高性能需求（如 RPC、MEV）或资源受限场景。  
6. **生产就绪**：已完成安全审计（Sigma Prime），适用于质押、高可用服务等关键场景。  

**注意事项**  
- Alpha 版本数据库需通过 `reth db drop` 重置后重新同步。  
- 测试需安装 Geth（部分测试可独立运行）。