
---
title: czkawka
---

### [qarmin czkawka](https://github.com/qarmin/czkawka)

**项目核心内容总结：**

**项目名称**  
Czkawka（波兰语“hiccup”）和Krokiet（波兰语“croquet”），均为用于清理计算机冗余文件的工具。

**核心功能**  
- 通过多种工具清理文件：查找重复文件（基于名称、大小或哈希）、大文件、空文件夹、临时文件、无效符号链接、损坏文件、扩展名不匹配文件等。  
- 支持相似图片/视频、音乐重复检测（基于标签或内容分析）。  
- 提供CLI（命令行）和GUI（GTK 4或Slint框架）两种界面。  

**主要特性**  
- 使用Rust编写，内存安全，几乎无Unsafe代码。  
- 跨平台（Linux、Windows、macOS、FreeBSD等）。  
- 支持缓存加速二次扫描，无广告，不收集用户数据。  
- 多语言（支持波兰语、英语、意大利语等）。  
- 开源（MIT许可证，Krokiet为GPL-3.0-only）。  

**使用方法**  
- CLI和GUI分别通过对应子项目（`czkawka_cli/README.md`、`czkawka_gui/README.md`）的文档安装和编译。  
- 通过[GitHub发布页面](https://github.com/qarmin/czkawka/releases)获取安装包或 nightly 构建版本。  

**其他信息**  
- 依赖`czkawka_core`库实现功能复用，支持第三方项目集成（如Python绑定）。  
- 捐赠链接：[https://github.com/sponsors/qarmin](https://github.com/sponsors/qarmin)。