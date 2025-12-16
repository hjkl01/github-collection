
---
title: universal-android-debloater
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/0x192/universal-android-debloater?style=social) ](https://github.com/0x192/universal-android-debloater)
### [0x192 universal-android-debloater](https://github.com/0x192/universal-android-debloater)

**核心内容总结：**  
本项目是一个用Rust重写的Android系统应用卸载工具（Universal Android Debloater GUI），旨在通过移除冗余系统应用提升隐私保护、电池续航和安全性。主要功能包括：卸载/禁用系统应用、支持多设备操作、导出/导入自定义卸载列表、操作日志记录，以及覆盖主流厂商（如Google、三星、华为等）和运营商的预装应用列表。  

**使用方法：**  
1. 备份手机数据，开启开发者选项及USB调试模式；  
2. 安装ADB工具（Linux/Mac/Windows对应不同安装方式）；  
3. 下载UAD GUI最新版本，通过ADB连接设备后运行；  
4. 根据预设列表或自定义规则选择卸载应用，操作后需注意厂商更新可能导致已卸载应用被重新安装。  

**注意事项：**  
- 无法彻底卸载需Root权限的系统应用，部分操作可能引发设备重启或需恢复出厂设置；  
- 中国用户可能需使用AOSP列表卸载特定厂商的闭源应用；  
- 项目处于早期开发阶段，存在风险，操作前务必确认应用功能，避免误删关键系统组件。