
---
title: moonlight-qt
---

### [moonlight-stream moonlight-qt](https://github.com/moonlight-stream/moonlight-qt)

**Moonlight PC 项目核心内容总结**  

**项目功能**  
Moonlight PC 是 NVIDIA GameStream 和 Sunshine 的开源 PC 客户端，支持跨平台流媒体传输，提供硬件加速视频解码、多格式编解码器（H.264/HEVC/AV1）、HDR、多点触控、游戏手柄支持、远程鼠标键盘控制等功能。  

**主要特性**  
- 支持 Windows、macOS、Linux、Raspberry Pi、ARM 设备等多平台；  
- 兼容多种编解码器及高级功能（如 YUV 4:4:4、7.1 环绕声、10 点触控）；  
- 提供 Steam Link 版本（分辨率最高 1080p，不支持 HDR）；  
- 支持通过系统快捷键（如 Alt+Tab）控制主机。  

**使用方法**  
- **下载**：提供 Windows/macOS 安装包、Snap/Flatpak/AppImage（Linux）、Raspberry Pi 及 ARM 设备安装指南；  
- **构建**：需 Qt 6.7 或更高版本，Windows 需 Visual Studio 2022，macOS 需 Xcode 14，Linux 需安装 Qt、FFmpeg 等依赖；  
- **开发贡献**：通过 GitHub 叉项目、提交代码及 Pull Request 参与开发。  

**注意事项**  
- Steam Link 版本存在硬件限制（如最大 1080p、40Mbps 带宽）；  
- 构建嵌入式版本需添加 `CONFIG+=embedded` 参数，部分平台可优化 GPU 性能。