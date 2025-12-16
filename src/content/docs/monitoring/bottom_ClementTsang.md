
---
title: bottom
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/ClementTsang/bottom?style=social) ](https://github.com/ClementTsang/bottom)
### [ClementTsang bottom](https://github.com/ClementTsang/bottom)

**项目功能**  
bottom 是一个用 Rust 编写的跨平台系统监控工具，可实时显示 CPU、内存、磁盘、网络等资源使用情况，并支持自定义监控指标和视图。用户可通过进程树查看详细信息，支持对进程排序、过滤及异常资源使用高亮显示，还提供插件扩展功能。

**使用方法**  
通过 `cargo install bottom` 安装，或从源码编译后运行 `bottom` 命令启动。支持命令行参数自定义监控项和显示方式。

**主要特性**  
1. 实时更新系统资源数据；  
2. 可自定义监控指标和视图布局；  
3. 进程树展示及进程管理（排序、过滤）；  
4. 异常资源使用高亮提醒；  
5. 插件系统支持功能扩展；  
6. 跨平台（Windows、Linux、macOS）兼容。  

项目灵感来源于 gotop、gtop 和 htop，依赖多个开源库，感谢贡献者及 JetBrains 的工具支持。