
---
title: rusty-kaspa
---

### [kaspanet rusty-kaspa](https://github.com/kaspanet/rusty-kaspa)  ![GitHub Repo stars](https://img.shields.io/github/stars/kaspanet/rusty-kaspa?style=social)

这是基于 Rust 实现的 Kaspa 全节点及辅助库项目，作为现有 Golang 节点的替代方案，是 Kaspa 网络推荐的节点软件。项目核心功能如下：

1. **节点运行**：支持主网、测试网及开发网节点启动，可配置 UTXO 索引、RPC 监听及共识参数。
2. **钱包系统**：提供命令行钱包接口，支持基于 WebAssembly (WASM) 的 Web 和 Node.js 钱包 SDK。
3. **通信协议**：集成 wRPC 子系统，支持 WebSocket 环境下的 JSON 或 Borsh 协议高性能 RPC。
4. **挖矿支持**：提供 Stratum Bridge Beta 版，允许矿工软件连接网络。
5. **构建部署**：支持 Linux、Windows、MacOS 原生编译及 Docker 多架构（amd64/arm64）镜像构建。
6. **开发测试**：内置网络模拟框架（Simpa）、单元测试、基准测试、内存分析及代码检查工具。
7. **网络适配**：支持网络硬分叉升级（如 Crescendo Hardfork），适配 10 BPS 出块率。