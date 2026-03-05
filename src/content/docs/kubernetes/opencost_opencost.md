
---
title: opencost
---

### [opencost opencost](https://github.com/opencost/opencost)  ![GitHub Repo stars](https://img.shields.io/github/stars/opencost/opencost?style=social)

OpenCost 是一款开源的 Kubernetes 和云支出监控工具，旨在提供当前与历史支出的可见性及成本透明度。它支持 AWS、Azure、GCP 等多云环境及本地集群，核心功能包括：实时按集群、节点、命名空间、Pod 等粒度进行成本分配；通过云厂商 API 实现动态定价监控；核算 CPU、GPU、内存、存储等资源成本及碳排放数据；支持 Prometheus 指标导出与外部成本集成。项目内置 MCP 服务器，允许 AI 代理通过标准化接口查询成本与资产数据。支持通过 Helm Chart 部署，兼容 K8s 1.20+，遵循 Apache 2.0 协议。