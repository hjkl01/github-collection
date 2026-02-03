
---
title: bitchat
---

### [permissionlesstech bitchat](https://github.com/permissionlesstech/bitchat)  ![GitHub Repo stars](https://img.shields.io/github/stars/permissionlesstech/bitchat?style=social)

**项目核心内容总结：**

**功能**  
BitChat 是一款去中心化点对点消息应用，采用双传输架构：**蓝牙Mesh网络**（用于离线通信）和**Nostr协议**（用于联网通信），无需账号、手机号或中心服务器。支持基于地理位置的聊天频道（如城市、区域等），并提供端到端加密、智能消息路由（蓝牙优先，Nostr备用）及紧急数据清除功能。

**使用方法**  
1. **Xcode 方式**：克隆项目后配置 `Local.xcconfig` 文件，设置 Bundle ID 和权限组，通过 Xcode 编译运行。  
2. **Just 工具**：安装 `just` 后，执行 `just run` 直接在 macOS 上运行。

**主要特性**  
- **双传输架构**：蓝牙Mesh（离线）+ Nostr（联网），支持多跳中继和地理位置频道（如 `block #dr5rsj7`）。  
- **隐私保护**：无账号系统，采用 Noise 协议（蓝牙）和 NIP-17 加密（Nostr），数据可三击清除。  
- **智能路由**：优先使用蓝牙直连，无蓝牙时通过 Nostr 全球中继网络传输。  
- **地理位置频道**：基于 geohash 精度划分区域（城市块、社区、国家等），支持全球范围聊天。  
- **优化功能**：LZ4 压缩、电池优化模式、支持 iOS 和 macOS。  

**技术架构**  
蓝牙Mesh用于本地离线通信（最大7跳中继），Nostr用于联网通信（通过290+全球中继节点），支持私聊和地理频道。