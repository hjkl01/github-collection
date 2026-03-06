
---
title: ServerStatus
---

### [cppla ServerStatus](https://github.com/cppla/ServerStatus)  ![GitHub Repo stars](https://img.shields.io/github/stars/cppla/ServerStatus?style=social)

ServerStatus 中文版是一个多服务器云探针与监控系统，核心功能如下：

1. **多节点监控**：实时采集并展示多服务器的 CPU、内存、硬盘、网络流量及连接状态等硬件资源数据。
2. **智能告警**：内置 Watchdog 触发式告警，支持自定义表达式规则（如负载、流量、宕机、DDoS 检测），可配置 Telegram、Server 酱、PushDeer 等回调通知渠道。
3. **网络探测**：支持 HTTP/HTTPS 域名连通性检测及 SSL 证书有效期监控。
4. **可视化面板**：提供 Web 界面实时展示监控数据、流量统计及服务器地理位置信息。
5. **灵活部署**：服务端支持 Docker、C++ 编译或手动部署；客户端支持 Python 跨平台运行（Linux/Windows/Mac），可配合 Docker 实现容器化部署。