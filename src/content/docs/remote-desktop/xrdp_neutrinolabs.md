
---
title: xrdp
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/neutrinolabs/xrdp?style=social) ](https://github.com/neutrinolabs/xrdp)
### [neutrinolabs xrdp](https://github.com/neutrinolabs/xrdp)

**项目核心内容总结：**

**功能**  
xrdp 是一个开源的 RDP 服务器，支持通过微软远程桌面协议（RDP）实现远程图形化登录，兼容多种客户端（如 Windows MSTSC、FreeRDP、KRDC 等）。默认使用 TLS 加密传输，支持连接 Linux 桌面、会话重连、屏幕缩放、RDP/VNC 代理等功能。

**主要特性**  
- 远程桌面：支持 Linux 桌面访问、会话恢复、动态调整屏幕大小、代理连接其他 RDP/VNC 服务器  
- 资源访问：双向剪贴板传输、音频/麦克风重定向（需额外模块）、本地驱动器挂载  
- 平台支持：主要面向 GNU/Linux 系统，适配 x86/x86-64 和 ARM 架构，部分功能需 x86 架构加速  

**使用方法**  
- **安装**：Ubuntu/Debian 使用 `apt install xrdp`，Fedora/RHEL 需先启用 EPEL 源后通过 `dnf install xrdp` 安装  
- **编译**：需安装 gcc、make、openssl-devel 等依赖，执行 `./bootstrap`、`./configure`、`make`、`sudo make install` 流程。音频重定向需额外构建模块  
- **配置**：确保防火墙开放 3389 端口，安装 xorgxrdp 以获得最佳体验（部分系统需手动安装 Xvnc 作为替代）