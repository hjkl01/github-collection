
---
title: LACT
---

### [ilya-zlobintsev LACT](https://github.com/ilya-zlobintsev/LACT)  ![GitHub Repo stars](https://img.shields.io/github/stars/ilya-zlobintsev/LACT?style=social)

**Linux GPU 控制应用程序核心内容总结：**

这是一个用于 Linux 系统上的 GPU 控制应用程序，支持 AMD、NVIDIA 和 Intel 显卡。其核心功能包括：

### 项目功能：
- **GPU 信息查询**  
  显示 GPU 型号、VBIOS 版本、显存信息、硬件单元信息、Resizable BAR 状态、Vulkan 特性等。
- **监控功能**  
  支持监控功耗、温度、频率，可配置历史图表并导出为 CSV。
- **电源配置**  
  设置功耗上限和电源状态（仅 AMD）。
- **散热控制**  
  自定义风扇曲线（AMD/NVIDIA），支持 RDNA3+ 的热控参数设置。
- **超频与欠压**  
  支持 GPU/显存频率调节，AMD 支持电压偏移欠压，NVIDIA 通过间接方式欠压。
- **配置文件管理**  
  根据运行程序或游戏模式自动切换配置文件。
- **远程管理**  
  可通过 TCP 连接远程管理 GPU（需手动配置，无加密）。
- **命令行支持**  
  提供 CLI 工具，支持列出 GPU、获取信息、切换配置文件等。

### 使用方法：
- 安装方式：支持 Arch、Debian/Ubuntu、Fedora、Gentoo、OpenSUSE、NixOS、Flatpak 等多种 Linux 发行版。
- 启动服务：`sudo systemctl enable --now lactd`。
- 使用 GUI 或 CLI 操作 GPU 设置。

### 主要特性：
- 支持多种 GPU 厂商；
- 提供丰富的监控和配置选项；
- 支持远程控制和命令行操作；
- 包含系统服务，不依赖图形界面；
- 支持多语言翻译，可通过 Weblate 参与本地化。

### 其他：
- 支持从源码编译；
- 提供硬件兼容性文档和常见问题解答；
- 可与 power-profiles-daemon 协同使用，避免冲突；
- 悬浮/恢复时自动重新加载设置（依赖 systemd）。