
---
title: lan-mouse
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/feschber/lan-mouse?style=social) ](https://github.com/feschber/lan-mouse)
### [feschber lan-mouse](https://github.com/feschber/lan-mouse)

**项目核心内容总结：**

**功能**  
Lan Mouse 是一款跨平台（支持 Windows、macOS、Linux）的局域网输入控制工具，可实现鼠标/键盘在多设备间的共享与控制，支持加密通信。

**主要特性**  
1. **图形界面**：基于 GTK + libadwaita，支持设备添加、授权、配置文件自动加载。  
2. **输入捕获与模拟**：  
   - 支持 Wayland（wlroots、libei）、Windows、macOS 的输入捕获；  
   - X11 输入捕获功能尚未完成。  
3. **安全性**：通过 TLS 证书指纹授权设备，加密传输数据。  
4. **智能管理**：自动检测设备状态，断开时释放按键，支持 IP 切换与端口自定义。  
5. **跨平台兼容**：适配 GNOME、KDE、Windows、macOS，支持远程桌面协议（xdp）。  

**使用方法**  
- **图形界面**：运行 `lan-mouse`，通过“Add”添加设备并授权；  
- **命令行**：使用 `lan-mouse cli` 管理连接；  
- **守护进程模式**：通过 `lan-mouse daemon` 后台运行，适配 systemd 服务。  

**配置**  
通过 `$XDG_CONFIG_HOME/lan-mouse/config.toml` 定义客户端位置、端口、授权指纹等参数。  

**注意事项**  
需确保 UDP 端口 4242（默认）开放，X11 输入捕获功能尚未完善。