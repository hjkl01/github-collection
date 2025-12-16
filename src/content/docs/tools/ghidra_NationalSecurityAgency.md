
---
title: ghidra
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/NationalSecurityAgency/ghidra?style=social) ](https://github.com/NationalSecurityAgency/ghidra)
### [NationalSecurityAgency ghidra](https://github.com/NationalSecurityAgency/ghidra)

Ghidra 是由美国国家安全局（NSA）开发的逆向工程分析框架，支持 Windows、macOS 和 Linux 多平台，具备反汇编、反编译、图形化分析、脚本开发等功能，可处理多种处理器指令集和可执行文件格式。用户可通过 Java 或 Python 开发扩展组件。

**使用方法**  
1. 安装 JDK 21，下载官方发布的 `ghidra_<版本>.zip` 文件并解压，运行 `ghidraRun`（或 `pyGhidraRun`）启动。  
2. 开发者需安装 Gradle、Python3、GCC/Clang 等工具，通过 `gradle buildGhidra` 构建开发版本。  
3. 扩展开发支持 Eclipse 插件（GhidraDev）或 Visual Studio Code，高级开发需使用 Eclipse 导入项目。

**主要特性**  
- 支持交互式与自动化分析模式  
- 提供脚本开发、图形化展示、多平台兼容性  
- 可扩展性高，允许用户自定义插件和工具  
- 官方提供安全公告，需注意版本漏洞风险