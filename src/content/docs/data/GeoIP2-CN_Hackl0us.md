
---
title: GeoIP2-CN
---

### [Hackl0us GeoIP2-CN](https://github.com/Hackl0us/GeoIP2-CN)  ![GitHub Repo stars](https://img.shields.io/github/stars/Hackl0us/GeoIP2-CN?style=social)

该项目提供一个小巧精悍、准确度高的 GeoIP2 数据库，专为代理工具判断中国大陆 IP 设计。数据整合自 ipip.net 和纯真 IP 库，仅包含中国大陆 IP 段，体积约 100KB，支持 CDN 分发及每 3 天自动更新。提供 CN-ip-cidr.txt 和 Country.mmdb 两种文件，分别适用于防火墙/老工具及 Surge、Clash 等主流代理软件。配置时需注意禁用冲突规则，且仅支持 GEOIP, CN 查询。