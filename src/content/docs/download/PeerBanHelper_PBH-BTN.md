
---
title: PeerBanHelper
---

### [PBH-BTN PeerBanHelper](https://github.com/PBH-BTN/PeerBanHelper)

**PeerBanHelper 核心内容总结：**

**项目功能**  
PeerBanHelper 是一款开源的个人网络防火墙工具，用于自动封禁异常、吸血或不受欢迎的 BT 客户端连接，支持自定义规则。主要功能包括：  
- 通过 Web API 获取连接信息并识别潜在威胁  
- 支持 PeerID、客户端名称、IP/GeoIP 等黑名单规则  
- 虚假进度检测、自动连锁封禁、多拨追猎等高级功能  
- 提供 WebUI 查看封禁列表、统计图表、规则订阅管理等  

**使用方法**  
1. 安装支持的客户端（如 qBittorrent 4.5.0+、Transmission 4.1.0+ 等），确保 Docker 容器使用 host 网络模式。  
2. 通过 WebUI 管理封禁规则、订阅 IP 规则库（推荐使用 BTN-Collected-Rules）。  
3. 安装后自动下载 GeoIP 数据库，支持按国家、网络类型等封禁 IP。  

**主要特性**  
- 支持多种 BT 客户端插件（需安装适配器）  
- GeoIP 分析与封禁（显示 IP 归属地、AS 信息等）  
- 提供本地数据分析、图表统计与历史封禁查询  
- 可结合 BTN 网络规则库提升效果（非必需）  

**注意事项**  
- Docker 安装需使用 host 网络驱动以获取真实 IP  
- 不支持 I2P/Tor 连接、BitComet 的 P2SP 功能  
- 需遵守软件声明，禁止用于非法活动