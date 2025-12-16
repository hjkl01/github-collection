
---
title: LSPosed
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/LSPosed/LSPosed?style=social) ](https://github.com/LSPosed/LSPosed)
### [LSPosed LSPosed](https://github.com/LSPosed/LSPosed)

**LSPosed Framework 核心内容总结：**  
LSPosed 是一个基于 Riru/Zygisk 的 ART 挂钩框架，提供与原始 Xposed 一致的 API，兼容 Xposed 模块并支持 Android 8.1 至 14 版本。其核心功能允许用户无需修改 APK 即可修改系统和应用行为，支持多模块协同工作，且变更仅在内存中生效，卸载后可恢复原系统。  

**使用方法：**  
1. 安装 Magisk v24+ 及 Riru v26.1.7+；  
2. 通过 Magisk 安装 LSPosed，重启后从通知栏打开管理器；  
3. 稳定版从 GitHub 发布页下载，测试版可通过 GitHub Actions 获取。  

**主要特性：**  
- 兼容 Xposed 模块，无需适配；  
- 基于 LSPlant 框架实现 ART 挂钩；  
- 支持多模块同时修改同一系统功能；  
- 提供中文翻译贡献渠道及 Telegram 社区支持。  

**注意事项：**  
- Bug 报告仅接受最新调试版；  
- GitHub Issue 标题需用英文；  
- 项目采用 GPL-3 许可证。