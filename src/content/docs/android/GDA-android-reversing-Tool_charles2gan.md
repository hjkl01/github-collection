
---
title: GDA-android-reversing-Tool
---

### [charles2gan GDA-android-reversing-Tool](https://github.com/charles2gan/GDA-android-reversing-Tool)  ![GitHub Repo stars](https://img.shields.io/github/stars/charles2gan/GDA-android-reversing-Tool?style=social)

GDA (GJoy Dex Analyzer) 是一款基于 C++ 开发的高效 Dalvik 字节码反编译及逆向分析平台，仅支持 Windows 系统，无需安装及 Java 环境。

核心功能涵盖：
1. 文件解析：支持 apk、dex、odex、oat、jar、class、aar 等多种文件格式。
2. 反编译与交互：支持 Java 与 Smali 互转，提供交叉引用、搜索、重命名、注释及代码保存功能。
3. 安全检测：包括恶意行为检测、隐私泄露扫描、静态漏洞扫描、加壳识别、敏感信息提取及 APK 取证。
4. 深度分析：提供污点分析（变量追踪与溯源）、路径求解（基于 LIR）、去混淆、调用图查看及 Smali 补丁重打包。
5. 辅助工具：支持 ODEX/OAT 提取 DEX、算法加解密、设备内存/文件提取、XML 解码，并集成 Frida Hook 及 Python/Java 脚本扩展。

使用方法：直接双击运行程序，拖入文件即可分析。