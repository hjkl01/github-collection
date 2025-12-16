
---
title: stacks-core
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/stacks-network/stacks-core?style=social) ](https://github.com/stacks-network/stacks-core)
### [stacks-network stacks-core](https://github.com/stacks-network/stacks-core)

**项目核心内容总结：**  
Stacks 是一个基于比特币的第二层区块链，使用比特币作为安全基础层，支持去中心化应用和可预测的智能合约（通过 Clarity 语言）。其核心特性是 **Proof of Transfer (PoX)** 机制，通过比特币区块链进行领导者选举，Stacks 矿工在独立的 Stacks 区块链上生成区块，无需修改比特币即可实现智能合约功能。

**使用方法：**  
1. **构建**：安装 Rust，克隆源码后执行 `cargo build --release`（或 `--profile release-lite` 优化内存占用）。  
2. **测试**：运行 `cargo test testnet` 或使用 `cargo nextest run` 并行执行单元测试（Windows 需单独运行测试）。  
3. **运行测试网**：通过 `cargo run --bin stacks-node -- start` 启动节点，配置文件路径为 `testnet-follower-conf.toml`。  

**主要特性：**  
- 依赖比特币安全性，通过 PoX 机制实现无需修改比特币的智能合约功能。  
- 支持 Clarity 语言开发可预测的智能合约。  
- 提供测试网运行环境及详细文档（包括发布流程、RPC 接口、事件调度等）。  
- 开源代码遵循 **GPLv3** 许可证，文档采用 **Creative Commons** 协议。