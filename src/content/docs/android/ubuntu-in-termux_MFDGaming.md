
---
title: ubuntu-in-termux
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/MFDGaming/ubuntu-in-termux?style=social) ](https://github.com/MFDGaming/ubuntu-in-termux)
### [MFDGaming ubuntu-in-termux](https://github.com/MFDGaming/ubuntu-in-termux)

**项目功能**：该脚本允许在Termux应用中无需root设备安装Ubuntu系统，当前支持Ubuntu 22.04版本，提供x86架构及Ubuntu 19.10分支选项。  

**使用方法**：  
1. 更新Termux并安装依赖（wget、proot、git）；  
2. 克隆脚本仓库至HOME目录，赋予执行权限；  
3. 运行`./ubuntu.sh -y`安装，随后通过`./startubuntu.sh`启动Ubuntu。  

**主要特性**：  
- 无需root权限；  
- 支持多版本Ubuntu分支；  
- 提供内核版本错误的解决方案（需手动修改脚本）。