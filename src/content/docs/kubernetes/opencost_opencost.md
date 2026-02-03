
---
title: opencost
---

### [opencost opencost](https://github.com/opencost/opencost)  ![GitHub Repo stars](https://img.shields.io/github/stars/opencost/opencost?style=social)

**项目名称：OpenCost**

**项目简介：**  
OpenCost 是一款开源的 Kubernetes 和云资源成本监控工具，帮助团队实时了解和分析 Kubernetes 集群及云服务的花费情况。它支持多种云平台（如 AWS、Azure、GCP）以及本地 Kubernetes 集群，并提供资源分配、成本归因和导出功能。

---

### **主要功能：**

- 实时按 Kubernetes 集群、节点、命名空间、控制器、服务或 Pod 分配成本
- 多云平台成本监控（AWS、Azure、GCP）
- 通过云平台计费 API 动态获取资产定价
- 支持本地 Kubernetes 集群的自定义 CSV 定价
- 分配 Kubernetes 内部资源（如 CPU、GPU、内存、持久卷）的成本
- 通过 `/metrics` 接口导出 Prometheus 指标
- 支持碳排放成本计算
- 支持 MCP（Model Context Protocol）协议
- 支持外部成本（如 Datadog）通过插件接入
- 开源免费（Apache 2.0 协议）

---

### **使用方法：**

OpenCost 仅支持通过 Helm 安装，安装命令如下：

```bash
helm repo add opencost https://opencost.github.io/opencost-helm-chart
helm repo update
helm install opencost opencost/opencost
```

> 注意：不推荐使用独立的 Kubernetes 清单文件安装，所有安装和升级均需通过 Helm。

---

### **MCP 服务器功能：**

OpenCost 提供 MCP 服务器，通过标准化接口为 AI 代理提供成本数据访问，支持以下功能：

- 成本分配查询（可过滤和聚合）
- 资产信息查询（节点、磁盘、负载均衡器等）
- 云成本查询（可按云服务商、服务类型、区域过滤）
- 支持 HTTP 协议传输
- 默认启用，运行在端口 8081

**配置方式：**

- 默认启用：无需额外配置
- 禁用：`--set opencost.mcp.enabled=false`
- 自定义端口：`--set opencost.mcp.port=9091`
- 调试模式：`--set opencost.mcp.extraEnv.MCP_LOG_LEVEL=debug`

---

### **其他使用方式：**

- **API 接口**：提供成本数据查询接口
- **CLI 工具**：支持 `kubectl cost` 命令行查询
- **Prometheus 集成**：支持导出指标到 Prometheus
- **用户界面**：通过 opencost-ui 提供可视化界面

---

### **支持的资产类型：**

- 节点（Node）
- 磁盘（Disk）
- 负载均衡器（LoadBalancer）
- 网络（Network）
- 云服务（Cloud）
- 集群管理（ClusterManagement）

---

### **社区与贡献：**

- 项目由 Kubecost 开发并开源
- 支持通过 CNCF Slack 的 `#opencost` 频道交流
- 每两周举行一次社区会议
- 接受社区贡献，详见 `CONTRIBUTING.md` 文件