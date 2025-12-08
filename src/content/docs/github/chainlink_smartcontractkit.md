
---
title: chainlink
---

### [smartcontractkit chainlink](https://github.com/smartcontractkit/chainlink)

**核心内容总结：**  
Chainlink 是一个开源的区块链预言机项目，为智能合约提供安全、去中心化的外部数据访问服务。其主要功能包括：  
1. **支持多链**：兼容以太坊、Polkadot、Cosmos 等多种区块链平台。  
2. **模块化架构**：通过外部适配器实现灵活扩展，支持自定义计算和 API 集成。  
3. **安全性**：提供密钥管理、官方镜像验证（使用 `cosign` 及 OIDC 签名）等功能。  

**使用方法**：  
- 安装依赖（如 PostgreSQL、pnpm 等），配置数据库连接。  
- 运行测试（通过 `go test` 及相关脚本）、构建代码（`make generate` 等）。  
- 部署时需验证官方镜像签名，确保来源可信。  

**主要特性**：  
- 支持社区驱动开发，提供详细的贡献指南。  
- 内置代码生成工具（mockery、gencodec）、测试框架（支持模糊测试、竞态检测）。  
- 支持 Nix 环境管理，确保开发环境的可复现性。