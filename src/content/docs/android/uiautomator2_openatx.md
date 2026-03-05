
---
title: uiautomator2
---

### [openatx uiautomator2](https://github.com/openatx/uiautomator2)  ![GitHub Repo stars](https://img.shields.io/github/stars/openatx/uiautomator2?style=social)

uiautomator2 是一个简单、易用且稳定的 Android 自动化 Python 库。

它通过设备端 HTTP 服务（基于 UiAutomator）与 Python 客户端通信，实现 Android 自动化控制。主要功能包括：

1. **设备连接与管理**：支持连接 Android 4.4+ 设备，获取设备信息、截图、屏幕尺寸及状态。
2. **UI 元素操作**：提供 XPath 和 Selector 定位方式，支持点击、滑动、拖拽、手势、文本输入及等待元素存在/消失。
3. **应用管理**：支持应用的安装、启动、停止、清除数据、获取信息及列表运行中的应用。
4. **系统交互**：支持剪贴板操作、按键事件、Toast 消息获取、弹窗监控（WatchContext）及应用会话管理。
5. **命令行工具**：提供截图、当前应用、安装、卸载等命令行功能。

项目依赖 android-uiautomator-server 和 adbutils。