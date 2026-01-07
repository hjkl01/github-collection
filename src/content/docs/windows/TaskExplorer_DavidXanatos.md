
---
title: TaskExplorer
---

### [DavidXanatos TaskExplorer](https://github.com/DavidXanatos/TaskExplorer)  ![GitHub Repo stars](https://img.shields.io/github/stars/DavidXanatos/TaskExplorer?style=social)

**TaskExplorer 核心内容总结：**  

**项目功能**：TaskExplorer 是一款任务管理工具，用于实时监控系统进程、资源使用情况及应用程序行为，提供深度系统分析能力。  

**主要特性**：  
- **多面板视图**：包含线程、内存、句柄、套接字、模块等面板，支持查看进程详细信息（如线程堆栈、内存编辑、文件句柄、网络连接等）。  
- **实时监控**：通过动态刷新展示 CPU、内存、磁盘、网络等系统资源使用情况，支持图表可视化。  
- **进程管理**：双击进程可单独窗口查看信息，支持卸载/注入 DLL、控制系统服务等操作。  
- **跨平台潜力**：基于 Qt 框架开发，当前支持 Windows 7 及以上系统，计划未来移植至 Linux。  

**使用方法**：  
- 启动后通过主界面查看进程列表，选中进程后下方面板显示详细信息。  
- 使用箭头键导航数据，双击进程可单独窗口查看。  
- 通过系统监控面板实时观察资源占用情况。  

**技术实现**：  
- 借助 Process Hacker 库及自编译的 SystemInformer 驱动实现系统监控功能。  
- 图标由 Icons8 提供，项目可通过 Patreon 支持。