### [loggie-io loggie](https://github.com/loggie-io/loggie)  ![GitHub Repo stars](https://img.shields.io/github/stars/loggie-io/loggie?style=social)

Loggie 是基于 Golang 的轻量级、高性能云原生日志代理和聚合器，用于构建可扩展的日志数据平台。

**核心功能：**
1. **云原生配置**：通过 Kubernetes CRD（LogConfig 等）声明式配置采集、处理及发送管道。
2. **多架构支持**：支持 Agent（DaemonSet）、Sidecar（自动注入）和独立 Aggregator 部署模式。
3. **高性能传输**：资源占用低，支持自适应 Sink 并发，根据下游状态动态调整传输。
4. **实时数据分析**：支持日志解析（JSON/Grok 等）、字段转换、条件处理、聚合计算及异常告警。
5. **可观测性**：提供丰富指标，支持一键接入 Grafana 及内置故障排查工具。