
---
title: Winhance
---

### [memstechtips Winhance](https://github.com/memstechtips/Winhance)  ![GitHub Repo stars](https://img.shields.io/github/stars/memstechtips/Winhance?style=social)

**Winhance - Windows Enhancement Utility**

**项目概述**
Winhance 是一款基于 C# 开发的 Windows 10/11 增强工具，旨在精简（Debloat）、优化和自定义系统体验。它能够在不重新安装 Windows 的情况下，提供与 UnattendedWinstall 类似的系统增强功能。本项目为独立开源项目，与微软官方无关。

**系统要求**
*   操作系统：Windows 10/11 (x64)
*   支持版本：Win 10 22H2, Win 11 23H2, 24H2, 25H2

**安装方法**
*   **PowerShell 一键安装**：运行命令 `irm "https://get.winhance.net" | iex`
*   **手动下载**：访问官网或 GitHub Releases 下载 `Winhance.Installer.exe`（安装程序同时包含可安装版和便携版）。

**核心功能**
1.  **软件与应用管理**
    *   **Windows 功能**：提供搜索界面，可一键安装/卸载 Windows 应用、遗留能力及可选功能。
    *   **外部应用**：集成 WinGet API，支持安装浏览器、多媒体工具、文档查看器等常用软件。
2.  **系统优化**
    *   可调节 UAC 通知级别、隐私设置、游戏性能、Windows 更新策略、电源计划、声音及通知偏好。
3.  **界面定制**
    *   支持切换 Windows 主题（深色/浅色），自定义任务栏、开始菜单和资源管理器外观。
4.  **高级工具**
    *   创建自定义 Windows ISO 镜像（支持注入当前系统驱动）。
    *   根据当前配置生成 autounattend.xml 自动应答文件。
5.  **配置管理**
    *   支持将当前设置保存为配置文件，方便在新系统或重装后快速还原配置。

**许可与支持**
*   **许可协议**：PolyForm Shield 1.0.0（免费用于个人及商业，禁止 Fork 后重新品牌化作为竞争产品分发）。
*   **社区反馈**：问题可提交至 GitHub Issues 或参与 Discord 社区讨论。
*   **项目状态**：目前处于开发中。