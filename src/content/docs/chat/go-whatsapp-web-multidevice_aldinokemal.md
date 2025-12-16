
---
title: go-whatsapp-web-multidevice
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/aldinokemal/go-whatsapp-web-multidevice?style=social) ](https://github.com/aldinokemal/go-whatsapp-web-multidevice)
### [aldinokemal go-whatsapp-web-multidevice](https://github.com/aldinokemal/go-whatsapp-web-multidevice)

**项目核心内容总结：**

本项目是一个基于Go语言的非官方WhatsApp通信工具，使用whatsmeow库实现，提供HTTP REST API和MCP协议接口，支持通过扫码登录、发送消息/文件/图片/视频/音频/投票/位置/联系人等操作，管理群组（创建、加入、修改群信息、管理成员）、处理用户隐私设置、读取/删除/编辑消息、标记消息星标等。  

**使用方法：**  
1. 安装依赖（如libpng、ffmpeg等）；  
2. 通过HTTP REST API或MCP协议调用功能（如扫码登录`/app/login`、发送消息`/send/message`）；  
3. Mac用户需设置环境变量`export CGO_CFLAGS_ALLOW="-Xpreprocessor"`以避免编译错误。  

**主要特性：**  
- 支持多平台（Windows/Mac/Linux）；  
- 提供丰富的API接口（含OpenAPI文档）；  
- 兼容MCP协议，支持AI工具集成；  
- 可独立运行REST API或MCP服务。  

**注意事项：**  
项目非官方，不建议用于商业场景，建议优先使用WhatsApp官方API。