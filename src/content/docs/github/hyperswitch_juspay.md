
---
title: hyperswitch
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/juspay/hyperswitch?style=social) ](https://github.com/juspay/hyperswitch)
### [juspay hyperswitch](https://github.com/juspay/hyperswitch)

**核心内容总结：**

**项目功能**  
Hyperswitch 是一个模块化的开源支付基础设施，支持企业按需选择集成模块（如智能路由、成本监控、支付保险库等），避免冗余和供应商锁定。提供支付模块的独立功能，包括费用审计、收入恢复、安全存储、多渠道支付支持等。

**使用方法**  
1. **本地部署**：通过 Docker 脚本一键启动，支持标准/完整/最小化部署模式。  
2. **云部署**：提供 AWS、GCP、Azure 的 Helm/CDK 部署方案，或通过 AWS CloudFormation 快速启动。  
3. **托管沙盒**：无需配置即可在线体验 Control Center、测试支付流程。

**主要特性**  
- **技术架构**：用 Rust 构建，保障性能与可靠性，支持全球支付方式（卡、钱包、BNPL、UPI 等）。  
- **模块化设计**：独立模块可灵活组合，如智能路由（提升首单成功率）、成本可观测性（费用审计）、收入恢复（自动重试策略）。  
- **工具支持**：提供可视化控制面板（Control Center）、自动化对账、安全支付数据存储（保险库）。  
- **开源与社区**：Apache 2.0 许可证，支持社区贡献，由 Juspay 团队维护（服务 400+ 企业）。