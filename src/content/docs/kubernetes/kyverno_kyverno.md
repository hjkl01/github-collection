
---
title: kyverno
---

### [kyverno kyverno](https://github.com/kyverno/kyverno)

**Kyverno 核心内容总结：**

Kyverno 是一个 Kubernetes 原生的策略引擎，通过策略即代码（Policy-as-Code）实现安全、合规、自动化和治理。其核心功能包括：
- **资源管理**：通过 Kubernetes 准入控制及后台扫描，实现资源验证、变异、生成和清理。
- **供应链安全**：验证容器镜像签名，确保来源合规。
- **工具兼容性**：支持 `kubectl`、`kustomize` 和 Git 等现有工具。

**使用方法：**
- 通过 [kyverno.io](https://kyverno.io) 获取安装指南、快速入门文档及策略库（含数百个生产级策略）。
- 支持通过策略库直接应用预定义规则，覆盖安全、运营、成本优化和开发规范等场景。

**主要特性：**
- **安全合规**：强制 Pod 安全标准、验证镜像来源、实施 CIS 基准政策。
- **运营优化**：自动打标签、生成默认配置（如 NetworkPolicy）、验证 YAML/Helm 清单。
- **成本控制**：限制资源配额、强制成本分配标签、清理冗余资源。
- **开发防护**：要求探针配置、验证镜像版本、自动注入配置信息。

**许可证**：Apache 2.0 开源协议，由 CNCF 孵化，原由 Nirmata 贡献。