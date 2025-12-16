
---
title: whatsapp-web.js
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/pedroslopez/whatsapp-web.js?style=social) ](https://github.com/pedroslopez/whatsapp-web.js)
### [pedroslopez whatsapp-web.js](https://github.com/pedroslopez/whatsapp-web.js)

**项目核心内容总结：**  
该项目是一个基于 WhatsApp Web 的 Node.js API 客户端，通过 Puppeteer 操作 WhatsApp 浏览器实现消息收发、媒体处理、群组管理等功能。  

**主要功能：**  
- 发送/接收文本、图片、音频、文档、视频（需 Chrome）、贴纸  
- 管理群组（创建、修改信息、添加/移除成员、设置权限）  
- 处理位置、联系人卡片、消息回复、状态消息、投票、频道等  
- 支持多设备登录  

**使用方法：**  
1. 通过 `npm i whatsapp-web.js` 安装  
2. 使用示例代码初始化客户端，扫描 QR 码登录  
3. 监听事件（如 `qr`、`ready`、`message`）实现功能逻辑  

**注意事项：**  
- 需 Node.js 18 及以上版本  
- 有被 WhatsApp 封禁风险（非官方客户端不被允许）  
- 视频发送依赖 Chrome 浏览器