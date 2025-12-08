
---
title: r0capture
---

### [r0ysue r0capture](https://github.com/r0ysue/r0capture)

### 项目核心内容总结

**项目功能**  
r0capture 是一个专为安卓平台设计的抓包工具，可绕过证书校验和加固机制，通杀 TCP/IP 应用层协议（如 HTTP、WebSocket、FTP、Protobuf 等）及主流框架（如 OkHttp、Retrofit 等），支持抓取明文和 SSL 加密流量，并可导出客户端证书。

**使用方法**  
1. **Spawn 模式**：启动应用时注入抓包逻辑，命令示例：`python3 r0capture.py -U -f 包名 -v`  
2. **Attach 模式**：附加到已运行的应用并保存抓包结果为 pcap 文件，命令示例：`python3 r0capture.py -U 应用名 -v -p 文件名.pcap`  
3. **功能选项**：  
   - `-H`：指定 Frida-Server 非标准端口连接；  
   - 支持定位应用收发包函数；  
   - 以 Spawn 模式运行可导出客户端证书（需提前授予存储权限）。

**主要特性**  
- 支持安卓 7-14 真机（不支持模拟器）；  
- 无视证书校验、加固壳（包括 VMP）；  
- 通杀应用层协议及框架；  
- 支持导出客户端证书（需 App 部署相关机制）；  
- 适配 Frida 16 及以上版本，兼容多平台（原项目基础）。  

**局限性**  
暂不支持 WebView、小程序、Flutter 等自研 SSL 框架，以及 HTTP/2/3 协议；不支持多进程（如 Service 子进程）抓包。