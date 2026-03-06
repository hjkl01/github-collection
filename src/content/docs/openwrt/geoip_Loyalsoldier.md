
---
title: geoip
---

### [Loyalsoldier geoip](https://github.com/Loyalsoldier/geoip)  ![GitHub Repo stars](https://img.shields.io/github/stars/Loyalsoldier/geoip?style=social)

本项目是一个 GeoIP 数据生成与管理工具，核心功能如下：

1.  **多格式文件发布**：每周四自动生成 V2Ray `dat`、MaxMind `mmdb`、sing-box `SRS`、mihomo `MRS`、Clash 及 Surge ruleset 等多种格式文件。
2.  **CLI 定制工具**：提供命令行接口，支持用户合并数据、转换格式、去重及查询 IP 类别。
3.  **数据优化增强**：基于 MaxMind GeoLite2 数据，融合中国大陆 IP 段，并新增 Cloudflare、Google、Netflix 等主流互联网厂商类别。
4.  **广泛软件兼容**：生成的文件适用于 V2Ray、Xray、Clash、mihomo、Surge、Hysteria、Nginx 等多种网络工具。
5.  **自定义生成**：支持通过 Fork 仓库配置自动化生成，或本地安装 CLI 工具手动定制。