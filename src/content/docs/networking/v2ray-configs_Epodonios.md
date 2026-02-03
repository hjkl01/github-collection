
---
title: v2ray-configs
---

### [Epodonios v2ray-configs](https://github.com/Epodonios/v2ray-configs)  ![GitHub Repo stars](https://img.shields.io/github/stars/Epodonios/v2ray-configs?style=social)

### 项目核心内容总结

#### **项目功能：**
该项目是一个 V2Ray 配置文件收集仓库，通过脚本每 5 分钟自动收集数千个 V2Ray 代理配置，支持多种协议，用户可直接使用这些配置文件或订阅链接来实现安全匿名的网络访问。

#### **支持协议：**
- Vmess
- Vless
- Trojan
- Tuic
- Shadowsocks
- ShadowsocksR

#### **使用方法：**
- 提供多种格式的配置链接（全部、按协议分类、分页列表等）。
- 用户只需将订阅链接复制到 V2Ray 客户端（如 v2rayng、fair、hiddify-next、nekoray 等）的订阅设置中，即可自动获取并更新配置。
- 可通过系统代理设置（如设置 IP 为 127.0.0.1，端口 10809）实现全系统代理，无需额外软件。

#### **附加功能：**
- 提供一个轻量级 Python 脚本，用于扫描和测试 V2Ray 配置的协议和延迟，可帮助用户筛选出响应更快的节点。
- 提供 Proxifier 激活码，用于设置系统级代理，实现全系统流量通过代理。

#### **主要特性：**
- 配置文件实时更新
- 支持多种主流代理协议
- 提供多种订阅方式（全量、按协议、分页）
- 提供配置测试工具（Python 脚本）
- 支持移动端和 PC 端使用
- 可实现系统级代理设置