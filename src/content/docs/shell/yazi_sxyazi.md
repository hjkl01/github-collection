
---
title: yazi
---

### [sxyazi yazi](https://github.com/sxyazi/yazi)  ![GitHub Repo stars](https://img.shields.io/github/stars/sxyazi/yazi?style=social)

**项目核心内容总结：**

Yazi 是一款基于 Rust 编写的终端文件管理器，采用非阻塞异步 I/O 技术，旨在提供高效、易用且可定制的文件管理体验。支持跨平台（macOS、Linux、Windows），当前为公开测试版，可能存在重大变更。

**主要功能与特性：**
1. **异步性能**：全异步 I/O 操作，多线程处理 CPU 任务，充分利用系统资源。
2. **图像预览**：支持多种终端协议（如 Kitty、iTerm2、WezTerm 等）的内联图像显示，兼容 Unicode 占位符和 Sixel 图形格式。
3. **插件系统**：支持 Lua 编写的 UI 插件、功能插件及自定义预览器/加载器，提供扩展性。
4. **虚拟文件系统**：支持远程文件管理及自定义搜索引擎。
5. **数据分发服务**：基于客户端-服务器架构，集成 Lua 发布-订阅模型，实现跨实例通信与状态持久化。
6. **包管理**：支持一键安装/更新插件和主题。
7. **集成工具**：兼容 ripgrep、fd、fzf、zoxide 等工具，支持 Vim 风格操作、多标签页、批量重命名、归档解压、Git 集成等。
8. **自定义与兼容性**：支持主题系统、鼠标操作、Trash 机制、自定义布局及 OSC 52 协议。

**使用方法：**
- 通过文档（[安装指南](https://yazi-rs.github.io/docs/installation)）安装。
- 支持命令行操作，集成终端常用工具，提供实时预览和跨目录选择功能。

**注意事项：**
- 项目处于活跃开发阶段，功能可能变动。
- 图像预览需依赖终端协议或第三方工具（如 Überzug++、Chafa）。