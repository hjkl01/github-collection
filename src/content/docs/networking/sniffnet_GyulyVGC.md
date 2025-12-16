
---
title: sniffnet
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/GyulyVGC/sniffnet?style=social) ](https://github.com/GyulyVGC/sniffnet)
### [GyulyVGC sniffnet](https://github.com/GyulyVGC/sniffnet)

**核心内容总结：**  
Sniffnet 是一款跨平台网络流量监控工具，支持 Windows、macOS 和 Linux 系统，提供实时流量分析、过滤、统计、图表可视化、自定义通知、PCAP 文件导出等功能。用户可通过选择网络适配器、设置过滤条件、查看实时流量图表、识别网络服务（如 6000+ 协议/服务）、查询域名和地理位置等操作，全面监控网络活动。  

**使用方法**：  
- 从 GitHub 发布页面下载对应系统的安装包；  
- 安装依赖项（如 libpcap/WinPcap 等）；  
- 启动后选择网络适配器并配置过滤规则；  
- 通过 Wiki 文档（[链接](https://github.com/GyulyVGC/sniffnet/wiki)）获取详细操作指南。  

**主要特性**：  
- 实时流量监控与图表展示；  
- 支持 PCAP 文件导出与导入；  
- 自定义通知规则（如特定流量触发警报）；  
- 识别远程主机的域名、ASN 和地理位置；  
- 支持本地网络连接分析及自定义主题；  
- 可保存常用网络主机并实时搜索分析连接。  

**注意事项**：  
- 部分系统需手动安装依赖库；  
- 若界面渲染异常，可设置环境变量 `ICED_BACKEND=tiny-skia` 切换渲染器。  

**其他**：  
项目依赖 [iced](https://github.com/iced-rs/iced) 库，IP 地理数据由 MaxMind 提供，支持通过官网及社交媒体（如 Bluesky、Telegram 等）获取更新信息。