
---
title: node_exporter
---

### [prometheus node_exporter](https://github.com/prometheus/node_exporter)  ![GitHub Repo stars](https://img.shields.io/github/stars/prometheus/node_exporter?style=social)

Node Exporter 是一款基于 Go 编写的 Prometheus 导出器，用于收集并暴露 *NIX 系统（Linux、BSD 等）的硬件及操作系统指标。该工具默认在 9100 端口监听，支持丰富的可插拔指标收集器，涵盖 CPU、内存、磁盘、网络、硬件监控等维度。支持 Docker 容器部署（需挂载宿主机文件系统）、Ansible 自动化安装及 TLS 加密。用户可灵活配置启用/禁用特定收集器、过滤指标范围或导出静态文本指标。Windows 系统建议使用专用的 Windows Exporter。