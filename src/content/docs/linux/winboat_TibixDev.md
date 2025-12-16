
---
title: winboat
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/TibixDev/winboat?style=social) ](https://github.com/TibixDev/winboat)
### [TibixDev winboat](https://github.com/TibixDev/winboat)

**项目核心内容总结：**

WinBoat 是一个允许在 Linux 系统上运行 Windows 应用的工具，通过容器化技术（Docker/Podman）和远程桌面协议实现无缝集成。主要功能包括：  
- **运行 Windows 应用**：支持运行任意 Windows 应用，以原生窗口形式嵌入 Linux 桌面。  
- **完整桌面体验**：可访问完整的 Windows 桌面环境或单独运行应用。  
- **文件共享**：Linux 家目录与 Windows 共享文件系统。  
- **自动化安装**：通过图形界面选择配置，简化安装流程。  

**使用方法**：  
- 下载 AppImage、.deb、.rpm 或解压版本，安装依赖（如 Docker/Podman、FreeRDP 3.x）。  
- 需启用系统虚拟化（KVM），并满足 4GB 内存、32GB 存储等硬件要求。  

**技术特性**：  
- 基于 Electron 开发，使用 FreeRDP 实现远程应用渲染。  
- 支持资源监控、智能卡直通等功能。  

**注意事项**：  
- 当前为测试版，可能存在 Bug，需自行排查问题。  
- Docker Desktop 不兼容，Podman 无法实现 USB 设备直通。  

**其他**：  
- 开源 MIT 许可证，支持社区贡献（禁止涉及敏感内容）。  
- 提供官网、社交媒体及 Discord 社区支持。