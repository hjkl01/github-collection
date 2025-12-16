
---
title: OpenClash
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/vernesong/OpenClash?style=social) ](https://github.com/vernesong/OpenClash)
### [vernesong OpenClash](https://github.com/vernesong/OpenClash)

**项目核心内容总结：**

OpenClash 是一个基于 OpenWrt 的 Clash 客户端插件，支持 Shadowsocks、Vmess、Trojan 等多种代理协议，通过灵活的规则配置实现策略代理。  

**使用方法：**  
1. 通过 GitHub 发布页下载 IPK 安装包；  
2. 或使用 OpenWrt SDK 编译源码，需依赖 luci、dnsmasq-full、iptables 等组件，编译后生成 IPK 文件安装。  

**主要特性：**  
- 基于 Luci For Clash 二次开发，兼容多种代理协议；  
- 支持 GEOIP 数据库、规则订阅、配置文件管理及运行日志查看；  
- 集成 Clash 核心功能与 Web 管理界面，可自定义策略组和规则。