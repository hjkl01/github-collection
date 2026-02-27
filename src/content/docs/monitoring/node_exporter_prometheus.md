
---
title: node_exporter
---

### [prometheus node_exporter](https://github.com/prometheus/node_exporter)  ![GitHub Repo stars](https://img.shields.io/github/stars/prometheus/node_exporter?style=social)

**项目核心内容总结：**

**项目名称：** node_exporter  
**项目功能：**  
node_exporter 是 Prometheus 的一个监控工具，用于收集 *NIX 系统（Linux、FreeBSD 等）的硬件和操作系统指标，支持通过 HTTP 接口暴露这些指标供 Prometheus 抓取。

**使用方法：**  
- 安装方式：支持直接下载、Ansible 自动化安装、Docker 部署等。  
- 默认监听端口：9100。  
- 启动方式：`./node_exporter`，或通过 Docker 容器运行。  
- Docker 部署示例中需挂载主机文件系统，并设置 `--path.rootfs` 参数。  
- 支持通过命令行参数启用或禁用特定的收集器（collector），如 `--collector.cpu`。

**主要特性：**  
- **支持多种操作系统**：包括 Linux、FreeBSD、OpenBSD、Darwin、Solaris 等。  
- **丰富的收集器（Collectors）**：默认启用许多常用指标收集器（如 CPU、内存、磁盘、网络等），也有部分默认禁用（如 perf、sysctl、tcpstat 等），用户可根据需要启用。  
- **可配置性高**：支持通过命令行参数或配置文件控制收集器的启用/禁用、过滤指标、设置 sysctl 收集规则等。  
- **支持 TLS**：可通过配置文件启用 HTTPS。  
- **文本文件收集器（textfile collector）**：允许将本地文件中的指标暴露出来，适用于批处理任务或静态标签。  
- **Docker 支持**：提供官方镜像，支持容器化部署，但需注意权限与文件挂载。  
- **过滤功能**：支持通过 `collect[]` 和 `exclude[]` 参数控制暴露的指标范围。

**附加说明：**  
- 支持 Windows 的替代方案为 windows_exporter，GPU 监控可用 dcgm-exporter。  
- 提供开发文档、测试方法及性能优化建议。