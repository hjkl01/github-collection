
---
title: whatsmeow
---

### [tulir whatsmeow](https://github.com/tulir/whatsmeow)

**项目简介**  
whatsmeow 是一个用于 WhatsApp Web 多设备 API 的 Go 语言库，支持消息收发、群组管理、状态同步等功能。

**核心功能**  
- 支持发送和接收私聊/群组消息（文本、媒体）  
- 管理群组及接收群组变更事件  
- 通过邀请链接加入群组、创建和使用邀请链接  
- 发送/接收打字状态、送达/已读回执  
- 读取和写入应用状态（联系人列表、聊天静音/置顶状态等）  
- 处理消息解密失败的重试机制  
- 发送状态消息（实验性功能，可能不支持大联系人列表）  

**未实现功能**  
- 发送广播列表消息（WhatsApp Web 本身不支持）  
- 通话功能  

**使用方法**  
通过 [godoc](https://pkg.go.dev/go.mau.fi/whatsmeow) 查看完整方法文档，[示例代码](https://pkg.go.dev/go.mau.fi/whatsmeow#example-package) 提供基础使用方式。  

**讨论渠道**  
- Matrix 房间：[#whatsmeow:maunium.net](https://matrix.to/#/#whatsmeow:maunium.net)  
- GitHub 讨论：[WhatsApp 协议 Q&A](https://github.com/tulir/whatsmeow/discussions/categories/whatsapp-protocol-q-a)