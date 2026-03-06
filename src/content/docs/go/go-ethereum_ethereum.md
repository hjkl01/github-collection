
---
title: go-ethereum
---

### [ethereum go-ethereum](https://github.com/ethereum/go-ethereum)  ![GitHub Repo stars](https://img.shields.io/github/stars/ethereum/go-ethereum?style=social)

Go Ethereum (geth) 是以太坊协议的 Golang 执行层实现。主要功能如下：

1. **节点运行**：支持全节点、归档节点和轻节点，可连接以太坊主网、测试网（如 Holesky）或搭建私有网络。
2. **API 接口**：内置 JSON-RPC 服务器，支持通过 HTTP、WebSocket 和 IPC 传输，供外部程序与以太坊网络交互。
3. **命令行工具集**：
   - `geth`：主客户端，用于区块链同步、账户管理及合约部署。
   - `clef`：独立签名工具，可作为 `geth` 的后端。
   - `abigen`：将智能合约定义转换为类型安全的 Go 包。
   - `evm`：EVM 虚拟机调试工具，支持字节码运行与断点调试。
   - `devp2p`：P2P 网络层交互工具。
   - `rlpdump`：RLP 数据格式转换与解析工具。
4. **部署与开发**：支持 Docker 快速部署，提供私有网络模拟环境（如 Simulated Backend 和 Dev Mode）。