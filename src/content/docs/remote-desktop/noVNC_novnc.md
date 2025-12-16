
---
title: noVNC
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/novnc/noVNC?style=social) ](https://github.com/novnc/noVNC)
### [novnc noVNC](https://github.com/novnc/noVNC)

**项目核心内容总结：**  
noVNC 是一个基于 HTML 的 VNC 客户端库和应用，支持现代浏览器（包括移动端 iOS/Android）。其主要功能包括：  
- **功能特性**：支持多种 VNC 认证方式（如 RSA-AES、Tight、VeNCrypt 等）、多种图像编码（如 H.264、JPEG、Zlib 等）、桌面缩放、剪贴板双向传输（含 Unicode）、多语言支持、触摸手势模拟鼠标操作等。  
- **使用方法**：通过 `novnc_proxy` 脚本启动代理服务，指定 VNC 服务器地址（如 `./utils/novnc_proxy --vnc localhost:5901`），然后在浏览器中访问生成的链接连接至 VNC 服务器。  
- **安装方式**：支持通过 Snap 包安装（`sudo snap install novnc`），并可作为系统服务运行，配置多个实例连接不同 VNC 服务器。  
- **服务器要求**：需支持 WebSockets 协议，若 VNC 服务器不支持，需配合 [websockify](https://github.com/novnc/websockify) 代理使用。  
- **浏览器兼容性**：推荐使用 Chrome 89+、Firefox 89+、Safari 15+ 等现代浏览器。