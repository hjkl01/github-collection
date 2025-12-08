
---
title: gopher64
---

### [gopher64 gopher64](https://github.com/gopher64/gopher64)

**项目核心内容总结：**  
gopher64 是一个支持 N64 游戏的跨平台模拟器，提供 Windows 和 Linux 安装包，亦可通过 Flatpak 安装。支持在线联机（Netplay）功能，可连接云服务器或自建局域网服务器进行多人对战。  

**使用方法：**  
- **下载安装**：Windows 用户可直接下载 `.exe` 文件，Linux 用户可通过 Flatpak 安装。  
- **便携模式**：在程序目录创建 `portable.txt` 文件，可将游戏数据存储于同一文件夹。  
- **命令行运行**：Linux 用户需安装 SDL3 和 Rust，通过 `cargo build` 构建后执行 `./target/release/gopher64 /path/to/rom.z64`。  

**主要特性：**  
- 默认支持键盘和 Xbox 手柄映射，可自定义控制方案。  
- 支持在线联机（需云服务器或自建服务器）。  
- 开源项目，基于 GPLv3 许可证，部分代码源自 mupen64plus 和 ares。  

**注意事项：**  
- 在线联机时服务器会记录 IP 地址和会话基础信息（游戏名称等），不存储其他个人数据。