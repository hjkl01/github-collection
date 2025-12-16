
---
title: GDA-android-reversing-Tool
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/charles2gan/GDA-android-reversing-Tool?style=social) ](https://github.com/charles2gan/GDA-android-reversing-Tool)
### [charles2gan GDA-android-reversing-Tool](https://github.com/charles2gan/GDA-android-reversing-Tool)

**项目核心内容总结：**  

**1. 项目功能**  
GDA（GJoy Dex Analyzer）是一款基于C++开发的Android反编译工具，支持对APK、DEX、ODX、OAT、JAR、CLASS、AAR等文件进行快速反编译与分析。主要功能包括：  
- **交互式操作**：支持跨引用、搜索、代码注释、重命名、保存分析结果等。  
- **辅助分析工具**：提取DEX文件、XML解码、算法工具、设备内存提取、路径求解、漏洞扫描等。  
- **高级特性**：恶意行为检测、隐私泄露扫描、静态漏洞分析、污点分析、反混淆、多DEX支持、API调用图谱查看等。  

**2. 使用方法**  
- 无需安装，直接双击运行程序。  
- 拖拽文件至GDA界面即可开始分析。  
- 对于JAR/CLASS文件需确保Java环境支持dx工具。  

**3. 主要特性**  
- **高效性**：C++实现，低内存与磁盘占用，支持快速反编译。  
- **多功能性**：集成恶意行为检测、漏洞扫描、路径求解、污点分析、反混淆等。  
- **便捷操作**：支持快捷键（如F5切换Java/Smali代码、X跨引用、S搜索等）。  
- **兼容性**：支持多DEX合并、Smali代码修改与APK重新打包。  

**4. 注意事项**  
- 项目非开源，部分工具和脚本可公开使用。  
- 可能被部分杀毒软件误报为病毒，需添加白名单。  
- 仅支持Windows平台，部分功能依赖Java环境。