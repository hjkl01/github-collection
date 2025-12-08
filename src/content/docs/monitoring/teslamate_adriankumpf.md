
---
title: teslamate
---

### [adriankumpf teslamate](https://github.com/adriankumpf/teslamate)

**核心内容总结：**  
TeslaMate 是一个用于特斯拉车辆的自托管数据记录工具，采用 Elixir 编写，使用 PostgreSQL 存储数据，并通过 Grafana 实现可视化与分析，同时支持通过 MQTT Broker 发布车辆数据。  

**主要功能与特性：**  
- **数据记录**：高精度记录驾驶数据，车辆在非使用时自动进入休眠状态，避免额外耗电。  
- **集成支持**：兼容 Home Assistant、Node-Red 和 Telegram（通过 MQTT），支持多车辆管理。  
- **地理围栏**：可自定义位置区域，跟踪车辆位置及行驶地图。  
- **充电管理**：记录充电成本，支持从 TeslaFi 和 tesla-apiscraper 导入数据。  
- **可视化**：提供丰富的 Grafana 仪表盘，涵盖电池健康、充电统计、驾驶效率、里程分析等。  

**使用方法：**  
通过 Docker 镜像部署，配置 PostgreSQL 数据库及 MQTT 服务，按文档指引完成安装与集成。