### [adriankumpf teslamate](https://github.com/adriankumpf/teslamate)  ![GitHub Repo stars](https://img.shields.io/github/stars/adriankumpf/teslamate?style=social)

TeslaMate 是一款功能强大的特斯拉自托管数据记录器。它采用 Elixir 开发，基于 Postgres 数据库存储数据，利用 Grafana 进行可视化分析与展示，并通过 MQTT 协议将车辆数据发布至本地 Broker。

核心功能如下：
- 高精度记录驾驶与充电数据，优化连接以减少车辆闲置耗电。
- 支持多车辆管理、自动地址解析、地理围栏及充电成本追踪。
- 内置丰富的仪表盘，涵盖电池健康、能耗效率、里程统计、驾驶详情、位置轨迹及车辆状态。
- 易于集成到 Home Assistant、Node-Red 及 Telegram 等系统。
- 支持从 TeslaFi 等平台导入历史数据。