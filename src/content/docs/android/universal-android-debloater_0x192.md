
---
title: universal-android-debloater
---

### [0x192 universal-android-debloater](https://github.com/0x192/universal-android-debloater)  ![GitHub Repo stars](https://img.shields.io/github/stars/0x192/universal-android-debloater?style=social)

这是一个基于 Rust 的 Android 去预装图形界面工具，旨在通过禁用或移除系统冗余应用以提升隐私、电池续航及安全性。

主要功能包括：
1. **应用管理**：支持禁用/恢复及导出/导入系统应用，记录操作日志。
2. **多支持**：支持多用户、多设备连接及主流厂商（如三星、小米等）与运营商的预装应用列表。
3. **安全机制**：无 Root 环境下仅能禁用应用；误删关键包可能导致无限重启（不会变砖），建议备份数据。
4. **运行环境**：需配合 ADB 工具并使用 USB 调试模式。