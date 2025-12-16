
---
title: erigon
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/erigontech/erigon?style=social) ](https://github.com/erigontech/erigon)
### [erigontech erigon](https://github.com/erigontech/erigon)

**项目核心内容总结：**  
Erigon 是一个高性能的区块链节点实现，支持多种同步模式（如快照同步）、数据库优化（使用 MDBX）和内存管理技巧。主要功能包括：  
1. **功能**：提供区块链数据同步、数据库存储、RPC 接口（通过 JSON-RPC 守护进程）及监控支持（集成 Prometheus 和 Grafana）。  
2. **使用方法**：  
   - 支持本地编译（Linux/macOS/Windows）或 Docker 部署，需配置数据目录、用户权限及环境变量。  
   - 可通过 `make` 命令构建，或使用 Docker Compose 启动容器化服务。  
3. **主要特性**：  
   - 优化数据库性能，支持大页内存分配、快照同步加速。  
   - 支持多平台（包括 Windows 本机编译、WSL2 环境）。  
   - 提供灵活的同步参数（如 `--sync.loop.block.limit`）和数据存储模式（如 `--prune.mode` 控制数据保留策略）。  
   - 可通过 Docker 容器化部署，简化依赖安装流程。