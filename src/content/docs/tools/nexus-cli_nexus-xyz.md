
---
title: nexus-cli
---

### [nexus-xyz nexus-cli](https://github.com/nexus-xyz/nexus-cli)

**项目核心内容总结：**

1. **项目功能**  
   Nexus CLI 是一个高性能命令行工具，用于向 Nexus 网络贡献计算证明，帮助统一全球节点的计算资源形成可验证的系统状态。

2. **使用方法**  
   - **安装方式**：  
     - 推荐使用预编译二进制文件：`curl https://cli.nexus.xyz/ | sh`  
     - 非交互式安装：通过脚本 `install.sh` 配合 `NONINTERACTIVE=1` 参数。  
     - Docker 部署：修改 `docker-compose.yaml` 中的节点 ID，执行 `docker compose up -d`。  
   - **操作流程**：  
     - 注册用户并绑定钱包地址：`nexus-cli register-user --wallet-address <地址>`  
     - 注册节点：`nexus-cli register-node --node-id <节点ID>`  
     - 启动 CLI：`nexus-cli start` 或指定难度参数（如 `--max-difficulty extra_large`）。  
     - 非交互模式：`nexus-cli start --headless`。  

3. **主要特性**  
   - **自适应难度系统**：根据节点性能自动调整任务难度（默认从 `small` 开始，完成时间短于 7 分钟则自动升级）。  
   - **难度分级**：支持 `small` 至 `extra_large_5` 等级别，适配不同硬件（如低资源设备用 `small`，高性能设备用 `extra_large` 以上）。  
   - **配置管理**：用户凭证存储于 `~/.nexus/config.json`，可通过 `nexus-cli logout` 清除。  

4. **其他信息**  
   - 项目遵循 **MIT** 和 **Apache 2.0** 双许可证。  
   - 首次使用需接受条款，支持通过 Discord 或 GitHub 提交问题。