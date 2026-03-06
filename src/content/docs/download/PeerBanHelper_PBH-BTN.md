
---
title: PeerBanHelper
---

### [PBH-BTN PeerBanHelper](https://github.com/PBH-BTN/PeerBanHelper)  ![GitHub Repo stars](https://img.shields.io/github/stars/PBH-BTN/PeerBanHelper?style=social)

PeerBanHelper 是一款开源的个人网络防火墙安全软件，旨在自动封禁不受欢迎、吸血及异常的 BT 客户端连接，并支持自定义规则。该软件通过支持的应用程序（如 BitTorrent 客户端）的 Web API 接口获取连接信息，识别潜在安全威胁并通知应用程序断开连接。核心功能包括 Peer ID 与 Client Name 黑名单、IP/GeoIP 及网络类型黑名单、虚假进度检查、自动连锁封禁、多拨追猎、伪装检查及主动监测。它支持网络 IP 集规则订阅，提供 WebUI 界面用于查看封禁名单、日志、统计图表及规则管理，并支持基于 GeoIP 库的 IP 归属地、ASN 及网络类型分析。兼容 qBittorrent、BiglyBT、Deluge、Transmission、BitComet 等主流客户端（需特定版本），仅支持传统 IPv4 或 IPv6 地址。