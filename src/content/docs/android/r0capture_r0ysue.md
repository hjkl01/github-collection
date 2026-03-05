
---
title: r0capture
---

### [r0ysue r0capture](https://github.com/r0ysue/r0capture)  ![GitHub Repo stars](https://img.shields.io/github/stars/r0ysue/r0capture?style=social)

r0capture 是一款基于 Frida 的安卓应用层抓包脚本，支持 Android 7 至 14 真机环境。核心功能包括：无视证书校验与绑定，通杀 HTTP、WebSocket 等应用层协议及 Okhttp、Retrofit 等网络框架，支持绕过应用加固。提供收发包函数定位、客户端证书导出、抓包保存为 pcap 格式及非标准端口连接等辅助功能。暂不支持 WebView、Flutter 等自定义 SSL 框架、HTTP/2/3 协议及模拟器环境。