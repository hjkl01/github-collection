
---
title: erigon
---

### [erigontech erigon](https://github.com/erigontech/erigon)  ![GitHub Repo stars](https://img.shields.io/github/stars/erigontech/erigon?style=social)

Erigon 是一个高效、模块化的以太坊执行层与嵌入式共识层客户端。
- **多链支持**：支持以太坊、Gnosis 和 Polygon 主网及测试网，默认为全节点，可配置为归档或最小化模式。
- **性能优化**：通过 OtterSync 实现快速同步，利用扁平化 KV 存储、快照和预处理技术优化状态存储与读写效率。
- **组件集成**：内置 Caplin 共识客户端，支持 PoS 验证器区块生产，提供 JSON-RPC、Grafana 监控及 MCP AI 集成。
- **灵活部署**：支持 Docker 容器化、源码构建及库调用，支持多实例运行和灵活的配置文件管理。