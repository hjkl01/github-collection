
---
title: cfnew
---

### [byJoey cfnew](https://github.com/byJoey/cfnew)  ![GitHub Repo stars](https://img.shields.io/github/stars/byJoey/cfnew?style=social)

**项目核心内容总结：**  
该项目是一个基于Cloudflare Workers的代理配置管理工具，支持多协议（VLESS/Trojan/xhttp）、自定义路径、实时配置和多语言界面。主要功能包括：  
1. **延迟测试**：内置IP延迟测试工具，支持手动输入、CF随机IP或远程URL获取IP，自动计算真实网络延迟并匹配中文机场名称。  
2. **多协议支持**：默认启用VLESS，可自定义开启Trojan或xhttp协议，客户端自动识别并适配最佳协议组合。  
3. **自定义路径**：通过`d`变量设置访问路径，替代UUID路径，提升隐蔽性与灵活性。  
4. **图形化配置**：通过`/{UUID或路径}`访问管理界面，实时保存配置到Cloudflare KV，无需重新部署。  
5. **API动态管理**：提供RESTful API接口（如添加/删除优选IP、查询列表），支持批量操作与自动合并数据。  
6. **多语言支持**：自动检测浏览器语言（中/波斯语），支持手动切换并持久化存储。  
7. **客户端适配**：兼容10种主流代理客户端（如CLASH、SURGE等），一键生成订阅链接并唤醒对应应用。  
8. **智能优选**：每15分钟自动优选IP，结合地区匹配、降级策略（CF失败时切换ProxyIP）保障稳定性。  

**使用方法**：  
- 通过图形界面配置协议、路径、优选IP等参数，实时生效。  
- 使用API接口（如`POST /api/preferred-ips`）批量管理IP列表。  
- 访问生成的订阅链接，客户端自动识别协议并应用配置。