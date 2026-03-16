### [juspay hyperswitch](https://github.com/juspay/hyperswitch)  ![GitHub Repo stars](https://img.shields.io/github/stars/juspay/hyperswitch?style=social)

Hyperswitch 是一个基于 Rust 构建的模块化开源支付基础设施，提供灵活且无供应商锁定的支付解决方案。其核心功能包括：

1. **成本可观测性**：监控和优化支付成本，识别隐藏费用与罚款。
2. **收入恢复**：基于智能重试策略减少被动流失，提供细粒度控制。
3. **金库服务**：提供 PCI 合规的卡片、令牌及银行凭证安全存储。
4. **智能路由**：根据预测成功率自动将交易路由至最合适的支付服务商。
5. **自动对账**：支持双向及三方对账自动化，降低人工操作成本。
6. **替代支付方式**：集成 PayPal、Apple Pay、Google Pay 及 BNPL 等支付方式。

项目支持 Docker 本地部署、云部署（AWS/GCP/Azure）以及托管沙箱环境，允许企业按需选择模块集成至现有支付栈。