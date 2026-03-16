### [winapps-org winapps](https://github.com/winapps-org/winapps)  ![GitHub Repo stars](https://img.shields.io/github/stars/winapps-org/winapps?style=social)

WinApps 是一个在 GNU/Linux 系统上无缝运行 Windows 应用程序的工具。它通过在 Docker、Podman 或 libvirt 虚拟机中运行 Windows，并利用 FreeRDP 将应用渲染为本地窗口，使其集成在 KDE Plasma、GNOME 或 XFCE 桌面环境中。

主要功能：
1. **应用支持**：支持几乎所有 Windows 应用程序（如 Microsoft 365、Adobe Creative Cloud），但不支持内核级反作弊系统。
2. **桌面集成**：在 Linux 桌面创建快捷方式，支持根据文件 MIME 类型右键调用 Windows 应用，自动打开 Office 链接。
3. **文件互通**：Windows 子系统可访问 Linux 的 `/home` 目录。
4. **辅助管理**：提供可选的 WinApps Launcher 用于虚拟机管理及应用启动。
5. **配置灵活**：支持自定义 RDP 参数、虚拟机后端及显示缩放比例。