### [prometheus prometheus](https://github.com/prometheus/prometheus)  ![GitHub Repo stars](https://img.shields.io/github/stars/prometheus/prometheus?style=social)

Prometheus 是 CNCF 旗下的系统和服务监控系统。它通过 HTTP 拉取模型定时从目标采集指标，支持利用 PromQL 查询语言对多维时间序列数据（由指标名和键值维度定义）进行查询、规则评估，并可根据条件触发告警。

核心特性如下：
1. **多维数据模型**：基于指标名称和维度键值定义时序数据。
2. **独立架构**：单节点独立运行，无分布式存储依赖。
3. **灵活采集**：支持静态配置或服务发现，亦可通过网关支持数据推送。
4. **可视化与联邦**：支持图表、仪表盘及层级和水平联邦功能。
5. **部署方式**：提供二进制包、Docker 镜像及源码构建，主要设计为独立程序使用。