
---
title: xonsh
---

### [xonsh xonsh](https://github.com/xonsh/xonsh)

**Xonsh 核心内容总结**  

1. **项目功能**  
   Xonsh 是一个 Python 驱动的跨平台 Shell，语言是 Python 3.6+ 的超集，支持 Python 语法和 Shell 原语（如变量、管道、命令执行等）。  

2. **使用方法**  
   - 安装：通过 `pip install 'xonsh[full]'` 安装。  
   - 使用：支持 Python 语法（如 `var = "hello".upper()`）与 Shell 命令（如 `cd $HOME`、`cat /etc/passwd | grep root`）混合编写脚本。  

3. **主要特性**  
   - **Python 与 Shell 融合**：可直接在 Shell 中使用 Python 表达式，或在 Python 中调用 Shell 命令（如 `len($(curl -L https://xon.sh))`）。  
   - **插件系统（Xontribs）**：支持扩展功能（如 `xontrib load dalias`），社区提供了大量插件（如 `xontrib-jupyter`）。  
   - **兼容性**：与 Conda、Starship、Zoxide 等工具集成，支持 Jupyter Notebook、终端交互环境（如 `euporie`）。  
   - **跨平台**：支持 Windows、Linux、macOS，提供 Docker、AppImage 安装方式。  

4. **社区与生态**  
   - 提供教程、速查表（Cheatsheet）和开发者指南。  
   - 社区贡献方式包括修复问题、开发插件、优化文档或设计 Logo 等。