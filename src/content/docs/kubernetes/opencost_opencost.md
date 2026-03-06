
---
title: opencost
---

### [opencost opencost](https://github.com/opencost/opencost)  ![GitHub Repo stars](https://img.shields.io/github/stars/opencost/opencost?style=social)

OpenCost 是一款开源的 Kubernetes 和云成本监控工具，旨在提供云支出和资源分配的现状与历史可见性。核心功能总结如下：

1. **多维度成本分摊**：支持按集群、节点、命名空间、Pod 等维度实时分摊 Kubernetes 及云资源成本（包括 CPU、GPU、内存、存储等）。
2. **多云与混合云支持**：集成 AWS、Azure、GCP 账单 API 实现动态定价，同时支持本地集群自定义 CSV 定价。
3. **数据集成与可视化**：提供 Web UI、API 及 CLI 工具，支持将定价数据导出至 Prometheus 指标，并包含碳排放成本计算。
4. **AI 集成能力**：默认内置 MCP 服务器，允许 AI 代理通过 HTTP 接口查询成本分配、资产及云成本数据。
5. **部署方式**：官方推荐使用 Helm Chart 在 Kubernetes 集群中进行安装和升级。