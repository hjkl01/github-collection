
---
title: rusty-kaspa
---

### [kaspanet rusty-kaspa](https://github.com/kaspanet/rusty-kaspa)

**项目核心内容总结：**

**项目功能：**  
Rusty Kaspa 是一个支持区块链的高性能节点实现，包含主网/测试网/开发网节点、钱包、CLI工具、模拟框架（Simpa）及Web钱包。支持UTXO索引、wRPC（WebSocket RPC）协议（JSON/Borsh）、基准测试和日志分析。

**使用方法：**  
- 启动节点：通过 `cargo run` 指定网络（主网/测试网/开发网）及参数（如 `--utxoindex`）。  
- 配置文件：使用 `--configfile` 指定配置文件，支持参数列表格式。  
- wRPC：启用 JSON/Borsh 协议，通过 `--rpclisten-json`/`--rpclisten-borsh` 设置监听地址。  
- 模拟测试：运行 `simpa` 生成虚拟区块，测试网络性能。  
- 钱包：通过 CLI 或 Web 界面操作，支持 WASM SDK 集成。

**主要特性：**  
- **高性能 wRPC**：支持 JSON 和 Borsh 编码，兼容 WebSocket 客户端。  
- **模拟框架（Simpa）**：生成虚拟 DAG，测试区块验证效率。  
- **UTXO 索引**：支持钱包功能及未花费交易输出查询。  
- **多协议支持**：兼容 JSON-RPC 1.0 和 Borsh 编码，适用于跨平台开发。  
- **可扩展性**：通过配置文件自定义共识参数，支持非主网环境实验。