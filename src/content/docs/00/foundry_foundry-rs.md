
---
title: foundry
---

### [foundry-rs foundry](https://github.com/foundry-rs/foundry)  ![GitHub Repo stars](https://img.shields.io/github/stars/foundry-rs/foundry?style=social)

**项目核心内容总结：**

Foundry 是一个基于 Rust 的开发工具链，主要用于以太坊智能合约的开发、测试和调试。它包括以下几个主要工具：

- **Forge**：用于编写和运行智能合约测试。
- **Cast**：用于与以太坊区块链进行交互，如查询余额、运行交易等。
- **Anvil**：一个快速的本地以太坊开发节点，支持链上数据的模拟和测试。
- **Chisel**：一个 Solidity 的交互式 REPL 工具，方便快速编写和测试代码。

**主要功能：**

- 支持 Solidity 合约的编写、测试、调试和部署。
- 提供对以太坊区块链的全方位交互能力。
- 支持链上数据的模拟和本地开发环境的搭建。
- 提供丰富的配置选项，支持多版本 Solidity 管理和多环境配置。

**使用方法：**

- 安装 Foundry：使用 `cargo install foundry` 命令。
- 初始化项目：使用 `forge init` 创建新项目。
- 编写测试：使用 Solidity 编写测试代码，并通过 `forge test` 运行。
- 使用 Cast 与链上数据交互。
- 使用 Anvil 启动本地节点：`anvil`。
- 使用 Chisel 进行交互式 Solidity 编码：`chisel`。

**主要特性：**

- 高度模块化和可配置。
- 支持快速编译和测试。
- 提供丰富的调试功能。
- 支持多 Solidity 版本管理。
- 可用于本地开发、测试和部署智能合约。