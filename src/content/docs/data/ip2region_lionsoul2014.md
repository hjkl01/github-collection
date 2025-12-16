
---
title: ip2region
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/lionsoul2014/ip2region?style=social) ](https://github.com/lionsoul2014/ip2region)
### [lionsoul2014 ip2region](https://github.com/lionsoul2014/ip2region)

### 核心内容总结

**项目功能**  
ip2region 是一个支持 IPv4 和 IPv6 的离线 IP 定位库及数据管理框架，提供高精度城市级 IP 定位，支持自定义地域信息（如 GPS、邮编等），并具备高效的数据存储和查询能力。

**主要特性**  
1. **离线定位**：内置 IPv4/IPv6 原始数据及预生成的 xdb 文件，支持城市级定位。  
2. **数据管理**：支持亿级 IP 段存储，允许自定义地域信息格式（如 `国家|省份|城市|ISP`）。  
3. **数据优化**：自动生成程序可合并连续 IP 段、去重压缩数据。  
4. **极速查询**：基于 xdb 文件的查询响应时间低至 10 微秒，支持内存缓存加速（vIndex 或全文件缓存）。  
5. **统一接口**：提供兼容的 API，同时支持 IPv4/IPv6 查询。  

**使用方法**  
- **查询**：通过多种编程语言（如 Java、Python、C++、PHP 等）的客户端实现查询，支持并发安全操作。  
- **数据生成**：使用各语言的生成工具（如 Java、Python、Rust）将原始 IP 数据转换为 xdb 文件。  
- **数据更新**：手动编辑原始数据文件（ipv4_source.txt/ipv6_source.txt）或通过检测算法自动更新。  

**支持语言**  
提供 Golang、Java、Python、C++、C#、Rust 等主流语言的查询和生成工具，部分语言由社区贡献（如 Ruby、Node.js）。  

**数据更新**  
原始数据需用户自行维护，可通过社区数据、GitHub Issue 或自定义数据更新，支持手动编辑或基于检测算法的自动化更新。  

**资源**  
提供官方社区（[ip2region.net](https://ip2region.net)）获取商用离线数据、文档、查询测试工具及数据纠错服务。