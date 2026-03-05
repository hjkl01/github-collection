
---
title: china-operator-ip
---

### [gaoyifan china-operator-ip](https://github.com/gaoyifan/china-operator-ip)  ![GitHub Repo stars](https://img.shields.io/github/stars/gaoyifan/china-operator-ip?style=social)

本项目是一个基于 BGP/ASN 数据构建的中国运营商 IP 地址库。

1.  **数据分类**：将 IP 地址按归属分类至各大国内运营商（如电信、移动、联通、教育网、科技网等）及特定服务商（如鹏博士、谷歌中国）。
2.  **数据获取**：提供每日自动更新的 CIDR 格式 IP 列表（支持 IPv4/IPv6），可通过 Git 仓库、EdgeOne Pages 或 GitHub Pages 站点直接获取；也支持用户本地利用 BGP 原始数据自行生成。
3.  **应用场景**：适用于 DNS 分域解析、网络流量按运营商出口分流、以及各类网络工具（如 Clash、V2Ray、smartdns 等）的 GeoIP 规则集制作。
4.  **开源许可**：项目代码与数据基于 MIT 协议开源。