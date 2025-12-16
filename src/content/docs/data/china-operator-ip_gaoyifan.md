
---
title: china-operator-ip
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/gaoyifan/china-operator-ip?style=social) ](https://github.com/gaoyifan/china-operator-ip)
### [gaoyifan china-operator-ip](https://github.com/gaoyifan/china-operator-ip)

**项目核心内容总结：**

1. **项目功能**  
   提供基于BGP/ASN数据的中国运营商IP地址分类库，支持按运营商（如中国电信、中国移动、中国联通等）划分IP地址，适用于网络路由分析、DNS解析分流等场景。

2. **使用方法**  
   - **直接获取**：通过GitHub或提供的链接下载预生成的CIDR格式IP列表（每日更新）。  
   - **自定义生成**：安装Rust工具链及依赖（如`bgpkit-broker`），执行`just`命令从BGP数据生成IP列表。

3. **主要特性**  
   - 数据源：结合BGP路由信息与ASN分析，避免WHOIS数据库的注册机构与实际使用不一致问题。  
   - 覆盖运营商：包含中国电信、中国移动、中国联通、教育网等主流运营商，部分运营商（如鹏博士、谷歌中国）为试验性支持。  
   - 开源免费：无商业付费限制，但覆盖率可能低于商业服务（如ipip.net）。  
   - 应用场景：可用于权威DNS分域解析、网络出口分流等（如[@ustclug](https://github.com/ustclug)项目）。  

4. **注意事项**  
   - 部分运营商（如中国铁通）数据已废弃，鹏博士IP可能由其他运营商代为宣告，存在覆盖不全情况。  
   - 若需完整国内IP集合，可参考[chnroutes2](https://github.com/misakaio/chnroutes2)项目。