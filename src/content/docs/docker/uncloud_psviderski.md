
---
title: uncloud
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/psviderski/uncloud?style=social) ](https://github.com/psviderski/uncloud)
### [psviderski uncloud](https://github.com/psviderski/uncloud)

**核心内容总结：**  
Uncloud 是一个容器编排工具，旨在简化分布式系统的管理。其核心功能包括：  
1. **无需控制平面**：通过 SSH 连接到任意节点即可管理集群，无需主节点或控制平面。  
2. **跨节点通信**：基于 WireGuard 的 overlay 网络实现 Docker 容器在不同机器间的直接通信。  
3. **分布式状态同步**：使用 Corrosion 分布式 SQLite 数据库同步集群状态，确保节点间数据一致性。  
4. **自动反向代理配置**：Caddy 反向代理自动检测新服务并更新路由规则，无需手动干预。  

**使用方法：**  
- 安装：通过 `brew install` 或源码编译安装。  
- 初始化集群：使用 `uncloud init` 创建集群。  
- 添加节点：通过 SSH 连接新机器并执行 `uncloud machine add`。  
- 部署服务：使用 `uncloud run` 指定服务名称、端口和镜像，自动分配节点并启动容器。  

**主要特性：**  
- 无中心化控制，节点可独立操作。  
- 自动扩展网络和状态同步，支持动态添加节点。  
- 简化部署流程，结合 CLI 与 SSH 实现高效管理。  

**注意事项：**  
项目目前处于开发阶段，功能可能频繁变动，不建议用于生产环境。