
---
title: geoip
---

### [Loyalsoldier geoip](https://github.com/Loyalsoldier/geoip)  ![GitHub Repo stars](https://img.shields.io/github/stars/Loyalsoldier/geoip?style=social)

**项目核心内容总结：**  
**功能**：  
- 提供IP/CIDR查询工具，支持多种文件格式（如文本、v2rayGeoIPDat等），可识别IP所属类别（如国家、运营商等）。  
- 支持本地文件与远程URL的查询，返回结果包括`true`、`false`或匹配的类别名称。  
- 支持批量处理IP/CIDR，适用于网络规则管理、地理定位等场景。  

**使用方法**：  
- 命令行模式：通过参数指定文件格式、路径及查询目标（如`./geoip lookup -f text -u ./cn.txt 1.0.1.1`）。  
- 交互模式（REPL）：输入IP/CIDR逐条查询，支持实时反馈与退出操作。  

**主要特性**：  
- 多格式兼容：支持文本、v2rayGeoIPDat等格式，适配多种项目需求（如Clash、Surge规则库）。  
- 高精度查询：基于MaxMind GeoLite2数据，覆盖全球IP范围。  
- 开源免费：采用CC-BY-SA-4.0和GPL-3.0双许可证，可自由使用与扩展。