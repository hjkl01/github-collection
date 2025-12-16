
---
title: KernelSU
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/tiann/KernelSU?style=social) ](https://github.com/tiann/KernelSU)
### [tiann KernelSU](https://github.com/tiann/KernelSU)

**KernelSU核心内容总结：**

KernelSU是一款基于内核的Android设备Root解决方案，主要功能包括：  
1. **内核级Root管理**：通过`su`实现系统权限控制。  
2. **模块化系统**：基于“metamodule”架构，支持无需系统修改的插件式功能扩展。  
3. **应用权限隔离**：通过“App Profile”机制限制应用的Root权限范围。  

**兼容性**：  
- 官方支持Android GKI 2.0设备（内核5.10+），兼容旧版内核（4.14+，需手动编译）。  
- 支持架构：`arm64-v8a`和`x86_64`。  
- 兼容WSA、ChromeOS及容器化Android。  

**使用方法**：  
- 提供[安装指南](https://kernelsu.org/guide/installation.html)、[编译教程](https://kernelsu.org/guide/how-to-build.html)及[官方文档](https://kernelsu.org/)。  

**其他**：  
- 翻译通过[Weblate](https://hosted.weblate.org/engage/kernelsu/)协作维护。  
- 许可证：`kernel`目录为GPL-2.0，其余部分为GPL-3.0。  
- 项目灵感源自Magisk等工具，部分功能借鉴了Kernel-Assisted Superuser等开源项目。