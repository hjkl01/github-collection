
---
title: uiautomator2
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/openatx/uiautomator2?style=social) ](https://github.com/openatx/uiautomator2)
### [openatx uiautomator2](https://github.com/openatx/uiautomator2)

**项目功能**  
uiautomator2 是一个基于 Python 的 Android 自动化测试库，支持应用安装/卸载、截图、启动/关闭应用、元素定位与操作（如点击、滑动）、权限管理、日志调试等功能，适用于 UI 测试和自动化脚本开发。

**使用方法**  
1. **Python API**：通过代码调用（如 `d.click()`、`d(text="登录").click()`）实现元素操作、应用控制等。  
2. **命令行工具**：支持通过 `uiautomator2` 命令执行截图、查看当前应用信息、安装/卸载应用等操作（如 `uiautomator2 screenshot`）。  

**主要特性**  
- 支持 Android 系统自动化测试，兼容多种设备和 Android 版本。  
- 提供丰富的 API，支持元素定位（文本、ID、层级等）、事件模拟、会话管理（Session）及异常检测（如应用崩溃）。  
- 集成 ADB 工具，支持与 Android 设备深度交互（如权限授予、日志调试）。  
- 提供命令行工具，便于快速执行常见操作。  
- 支持通过 `with` 语句管理应用会话，自动处理应用启动与关闭。