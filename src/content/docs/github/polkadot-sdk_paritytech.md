
---
title: polkadot-sdk
---

### [paritytech polkadot-sdk](https://github.com/paritytech/polkadot-sdk)

**项目核心内容总结**  
Polkadot SDK 是用于构建 Polkadot 多链区块链平台的工具包，提供构建区块链、平行链及跨链通信所需的所有组件。  

**功能与特性**  
1. **多链互操作性**：支持不同区块链之间的安全、可扩展的信息共享。  
2. **模块化架构**：集成 Substrate、FRAME、Cumulus 和 XCM 等核心组件，支持自定义区块链开发。  
3. **文档与工具**：提供详细的开发指南、Rust API 文档、项目模板及依赖管理工具 `psvm`。  
4. **构建支持**：支持 WASM 和 PolkaVM 目标架构，适配不同开发场景。  

**使用方法**  
- **快速启动**：通过脚本一键运行示例节点：  
  `curl --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/paritytech/polkadot-sdk/master/scripts/getting-started.sh | bash`  
- **构建依赖**：需安装 Rust 等工具，按文档指引配置环境。  
- **版本管理**：使用 `psvm` 工具统一管理 SDK 依赖版本。  

**社区与支持**  
提供 Telegram、Matrix、Discord 等社区渠道，及 StackExchange 技术问答支持。