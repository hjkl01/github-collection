
---
title: infracost
---

### [infracost infracost](https://github.com/infracost/infracost)  ![GitHub Repo stars](https://img.shields.io/github/stars/infracost/infracost?style=social)

**项目核心内容总结：**

Infracost 是一个支持 Terraform 的云成本估算工具，帮助工程师在部署前了解资源的云成本和 FinOps 最佳实践。它可在终端、VS Code 或 Pull Request 中使用，提供清晰的成本分解和比较。

**主要功能：**

- **成本估算**：根据 Terraform 配置估算 AWS、Azure、Google 云资源的成本，支持超过 1100 种资源。
- **命令支持**：
  - `infracost breakdown`：显示详细成本分解。
  - `infracost diff`：比较当前状态与计划状态的月度成本差异。
- **CI/CD 集成**：支持在 GitHub Actions 等平台中集成，自动在 Pull Request 中展示成本估算。
- **Infracost Cloud（SaaS 产品）**：提供云服务，支持团队设置标签策略、成本控制规则（Guardrails）等，提升 FinOps 实践效率。

**使用方法：**

- 通过官方文档的“快速入门”指南开始使用。
- 支持开源社区贡献，可通过 GitHub 参与开发。

**其他支持：**

- 支持使用量计费资源（如 AWS Lambda、S3）的成本估算。
- 社区活跃，提供 Slack 和 YouTube 等交流渠道。

**授权协议：** Apache License 2.0