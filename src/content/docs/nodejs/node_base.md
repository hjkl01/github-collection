
---
title: node
---

### [base node](https://github.com/base/node)

**项目功能**  
Base Node 是基于 Optimism OP Stack 构建的以太坊 L2 网络（Base）的节点软件，支持运行主网和测试网节点，提供安全、低成本的区块链服务。

**使用方法**  
1. 准备 Ethereum L1 全节点 RPC 接口。  
2. 根据网络选择 `.env.mainnet`（主网）或 `.env.sepolia`（测试网）配置文件，设置 L1 的 ETH RPC、Beacon 节点等参数。  
3. 通过 Docker Compose 启动节点，支持指定客户端（reth、geth、nethermind）和网络环境，例如：  
   ```bash  
   docker compose up --build  
   ```  
   或  
   ```bash  
   NETWORK_ENV=.env.sepolia CLIENT=reth docker compose up --build  
   ```  

**主要特性**  
- **支持客户端**：默认使用 `reth`，兼容 `geth` 和 `nethermind`。  
- **硬件要求**：至少 32GB 内存（推荐 64GB）、NVMe SSD 存储，生产环境推荐 AWS i7i.12xlarge 实例。  
- **配置选项**：支持 L1 接口类型（如 Alchemy、Infura）、缓存优化、快照同步等。  
- **网络支持**：主网和测试网均可用，主网默认使用 `https://mainnet-sequencer.base.org` 作为排序器。  
- **快照同步**：提供快照链接加速节点同步（详见官方文档）。