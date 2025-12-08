
---
title: douyinLive
---

### [jwwsjlm douyinLive](https://github.com/jwwsjlm/douyinLive)

### 项目核心内容总结

**功能**  
该项目通过WebSocket抓取抖音直播间弹幕和礼物数据，支持单进程监控多个直播间，数据以JSON格式输出。

**使用方法**  
1. 运行命令：`go run main/main.go --room 抖音直播间号 --port 端口号（默认18080）`，或编译后使用`main.exe --room 抖音直播间号`。  
2. 客户端通过`ws://127.0.0.1:1088/ws/直播间ID`连接，例如`ws://127.0.0.1:1088/ws/AAAAA`。  
3. 客户端需每30秒发送一次`ping`心跳包以维持连接。

**主要特性**  
- 单进程支持多直播间监控  
- 数据输出为JSON格式（需自行解析）  
- 内置心跳包机制  
- 可通过`--unknown`参数控制是否输出未解析数据（默认不输出）  

**其他说明**  
- Proto文件需完善（提供相关链接供参考）  
- 默认端口为18080，可自定义修改