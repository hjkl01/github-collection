
---
title: avalanchego
---

### [ava-labs avalanchego](https://github.com/ava-labs/avalanchego)

**项目功能**：AvalancheGo 是 Avalanche 区块链网络的节点实现，支持高吞吐量和快速交易，提供主网、测试网（Fuji）及本地测试网的连接能力。  

**使用方法**：  
1. **安装方式**：支持从源码构建（需 Go 1.24.9+）、APT 仓库安装、二进制文件下载或 Docker 镜像构建。  
2. **运行节点**：通过命令行启动主网或 Fuji 测试网节点，或使用 `avalanche-cli` 工具创建本地测试网。  

**主要特性**：  
- **轻量级协议**：最低硬件要求为 8 核 CPU、16GB 内存、1TB 存储，支持 Ubuntu 22.04/24.04 或 macOS 12+。  
- **引导过程**：新节点接入主网需数日完成数据同步（Bootstrapping），性能瓶颈通常为数据库 I/O。  
- **版本管理**：遵循语义化版本（`v0.x.x` 开发版，`v1.x.x` 生产版），接口可能随补丁版更新变化。  
- **支持平台**：Tier 1（Linux amd64 全面支持）、Tier 2（Linux/ARM64 部分支持），Windows/macOS（amd64）暂不支持。  

**其他**：提供 Protobuf 和 Mock 代码生成工具，支持社区安全漏洞报告（需遵循披露政策）。