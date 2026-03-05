
---
title: cadvisor
---

### [google cadvisor](https://github.com/google/cadvisor)  ![GitHub Repo stars](https://img.shields.io/github/stars/google/cadvisor?style=social)

cAdvisor (Container Advisor) 是一个运行时守护进程，旨在帮助用户理解运行中容器的资源使用和性能特征。它负责收集、聚合、处理并导出容器的资源隔离参数、历史资源使用量、直方图及网络统计信息，支持容器级别和机器级别的数据。

cAdvisor 原生支持 Docker 容器，并基于 lmctfy 容器抽象支持其他容器类型。支持多种部署方式，包括 Docker 容器、独立运行及 Kubernetes DaemonSet。项目提供 Web UI、版本化远程 REST API、存储插件导出支持以及官方 Go 客户端。其未来规划包括提供容器性能建议、基于建议的自动调优以及向调度层提供使用量预测。