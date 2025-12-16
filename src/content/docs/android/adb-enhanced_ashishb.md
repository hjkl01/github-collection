
---
title: adb-enhanced
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/ashishb/adb-enhanced?style=social) ](https://github.com/ashishb/adb-enhanced)
### [ashishb adb-enhanced](https://github.com/ashishb/adb-enhanced)

**核心内容总结：**

adb-enhanced 是一个增强 Android 调试桥（ADB）功能的命令行工具，提供以下核心功能：  
1. **设备与系统管理**：查看设备信息（如型号、系统版本）、管理应用（安装/卸载/备份）、调整系统设置（如屏幕亮度、动画开关、电池模式等）。  
2. **文件操作**：支持文件传输（拉取/推送文件）、目录浏览、文件删除与重命名。  
3. **应用与权限管理**：查看应用详细信息（版本、权限、安装时间）、管理运行时权限（授予/撤销）、备份应用数据为通用格式（tar）。  
4. **调试辅助**：截图、录屏、调试应用性能（如卡顿分析）、模拟用户操作（按键、输入文本、旋转屏幕）。  

**使用方法**：通过 `adbe` 命令加具体子命令和参数操作，例如：  
- `adbe app backup com.example app_backup.tar` 备份应用数据；  
- `adbe screenshot screenshot.png` 截图保存；  
- `adbe permissions grant com.example storage` 授予应用存储权限。  

**主要特性**：  
- 支持 Python3，兼容现代开发环境；  
- 提供丰富的 ADB 命令扩展，简化复杂操作；  
- 跨平台支持（可通过 Homebrew 安装）；  
- 包含测试与发布流程，便于社区协作维护。