
---
title: evcc
---

### [evcc-io evcc](https://github.com/evcc-io/evcc)

**evcc** 是一个可扩展的电动汽车充电控制器和家庭能源管理系统，旨在通过本地能源管理（无需依赖云服务）实现高效能管理。  

**核心功能与特性**：  
1. **设备兼容性**：支持多种电动汽车充电器（如 ABB、Tesla、Wallbox 等）、智能开关（如 Home Assistant、TP-Link）、热泵及电加热器（如 Bosch、Viessmann）、电能表（如 SMA、Victron）及车辆品牌（如 BMW、Tesla）。  
2. **灵活扩展**：通过插件系统（Modbus、MQTT、JavaScript 等）支持自定义设备集成。  
3. **通知与监控**：支持 Telegram、PushOver 等通知方式，结合 InfluxDB 和 Grafana 实现数据可视化。  
4. **开放接口**：提供 REST 和 MQTT API 供智能家居系统集成，并兼容 Home Assistant 和 openHAB。  

**使用方法**：通过项目文档（[链接](https://docs.evcc.io/en/)）获取配置和操作指南。  

**其他**：项目采用 MIT 许可证，部分赞助组件需单独授权；开发依赖社区和厂商支持，部分功能需赞助令牌维持。