
---
title: go-ethereum
---

### [ethereum go-ethereum](https://github.com/ethereum/go-ethereum)

**项目核心内容总结：**  

**项目功能**：Go Ethereum 是以太坊协议的 Golang 实现，提供全节点、存档节点和轻节点功能，支持运行主网、测试网及私有网络，提供 JSON-RPC 接口供外部程序交互。  

**使用方法**：  
- **构建**：需安装 Go 1.23+ 和 C 编译器，通过 `make` 命令构建。  
- **运行**：使用 `geth` 命令启动节点，支持主网（`--mainnet`）和测试网（如 `--goerli`）；通过配置文件或命令行参数自定义网络设置。  
- **私有网络**：需配合信标链，可使用模拟后端、Dev Mode 或 Kurtosis 工具搭建。  
- **Docker 快速启动**：提供预配置镜像简化部署。  

**主要特性**：  
- **多模式支持**：全节点、存档节点、轻节点灵活切换。  
- **接口丰富**：通过 HTTP、WebSocket 和 IPC 提供 JSON-RPC 接口（需手动启用），支持标准 API 和 `geth` 特有 API。  
- **开发工具**：包含 `clef`（安全密钥管理）、`devp2p`（P2P 协议测试）等辅助工具。  
- **安全性**：默认启用 IPC 接口，HTTP/WebSocket 需手动配置并限制访问域，防范攻击。  

**贡献与许可**：  
- 开源协议：库代码使用 LGPL-3.0，二进制文件使用 GPL-3.0。  
- 贡献方式：需遵循 Go 编码规范，提交 PR 至 `master` 分支，复杂变更需提前与核心开发者沟通。  
- 网站内容：独立维护，提交至 `website` 分支。