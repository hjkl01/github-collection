
---
title: AppPorts
---

### [wzh4869 AppPorts](https://github.com/wzh4869/AppPorts)  ![GitHub Repo stars](https://img.shields.io/github/stars/wzh4869/AppPorts?style=social)

**AppPorts 项目核心总结**

**项目简介**
AppPorts 是一款专为 macOS 设计的应用迁移与链接工具。旨在解决 Mac 内置存储空间不足的问题，支持用户将大型应用程序（如 Xcode、游戏等）一键迁移至外部存储设备（SSD、SD 卡、NAS），同时保留本地有效的“应用入口”，确保系统仍将其视为本地应用并可正常启动。

**核心功能与特性**
*   **应用瘦身**：支持多 GB 级应用的单键迁移，本地仅占用目录元数据（ negligible size）。
*   **兼容性优化**：采用优化的 `Contents` 链接策略，Finder 中无错误箭头图标，完美兼容 Launchpad 及系统菜单。
*   **安全与恢复**：自动锁定系统应用防止误删，迁移前检查运行状态，支持一键恢复至本地磁盘。
*   **用户体验**：SwiftUI 原生开发，支持深色模式、多语言（20+ 种）及内置搜索。
*   **无障碍支持**：优化 VoiceOver 朗读，支持 Braille（盲文）显示及语义化 UI。
*   **故障修复**：提供终端命令解决因签名导致的“应用已损坏”问题。

**使用与安装**
*   **系统要求**：macOS 14.0 (Sonoma) 或更新版本。
*   **权限配置**：首次运行需在系统设置中为 AppPorts 开启“完全磁盘访问”权限。
*   **开发支持**：项目基于 MIT 协议开源，支持通过 Xcode 构建源码。