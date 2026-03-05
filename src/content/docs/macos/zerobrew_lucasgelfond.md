
---
title: zerobrew
---

### [lucasgelfond zerobrew](https://github.com/lucasgelfond/zerobrew)  ![GitHub Repo stars](https://img.shields.io/github/stars/lucasgelfond/zerobrew?style=social)

zerobrew 是一款面向 macOS 和 Linux 的 Homebrew 性能优化客户端，采用 uv 风格架构。它利用内容寻址存储去重、APFS 零开销复制及基于 Ruby DSL 的源码构建回退技术，显著提升软件包安装与运行速度（冷启动提升 2 倍，热启动提升 7.6 倍）。该工具完全依赖 Homebrew 的公式定义、预编译包及基础设施，通过 zb 命令支持单包/多包安装、依赖文件管理、卸载及资源清理。目前为实验性项目，建议与原生 Homebrew 共存运行而非直接替代。