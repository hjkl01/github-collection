
---
title: OpenGFW
---

### [apernet OpenGFW](https://github.com/apernet/OpenGFW)

**项目核心内容总结：**

**项目名称**：OpenGFW（开源DIY中国防火墙工具）  
**功能**：基于Linux的网络流量过滤系统，支持IP/TCP重组、多种协议分析（HTTP/TLS/QUIC/DNS/SSH等）、加密流量检测（如Shadowsocks、Trojan）、机器学习流量分类、IPv4/IPv6、多核负载均衡、连接卸载、规则热重载（SIGHUP触发）等。  

**主要特性**：  
- 支持流量分析、拦截与日志记录（仅日志模式）  
- 基于[expr](https://github.com/expr-lang/expr)的规则引擎，支持复杂规则匹配  
- 可扩展IO实现（当前仅支持NFQueue）  
- 可用于广告拦截、家长控制、VPN滥用防护等场景  

**使用方法**：  
- 通过规则引擎配置过滤策略  
- 支持热重载规则（无需重启服务）  
- 部署于Linux系统（如家庭路由器）  

**注意事项**：  
- 项目处于早期开发阶段，功能可能不完善，使用需谨慎  
- 提供中文/日文文档（[中文文档](README.zh.md)）  
- 文档网站：https://gfw.dev/，Telegram交流群：https://t.me/OpGFW