### [mikavilpas yazi](https://github.com/mikavilpas/yazi)  ![GitHub Repo stars](https://img.shields.io/github/stars/mikavilpas/yazi?style=social)

Yazi 是一款基于 Rust 编写、采用非阻塞异步 I/O 的终端文件管理器。

**核心功能总结：**
1. **高效异步架构**：全异步 IO 操作，多线程 CPU 任务调度，内置图像解码与代码高亮，支持预加载机制加速文件加载。
2. **图像预览**：内置支持 kitty、iTerm2、Sixel 等多种终端图像协议，兼容 X11/Wayland 环境。
3. **插件系统**：支持 Lua 编写的并发插件，可自定义 UI 界面、功能逻辑、预览器及预加载器。
4. **工具集成**：深度集成 fd、rg、fzf、zoxide 等工具以提升搜索与导航效率。
5. **交互体验**：提供 Vim 风格操作、路径自动补全、多标签浏览、跨目录选择及可滚动预览（支持视频、PDF 等）。
6. **管理功能**：支持批量重命名、可视模式、文件选择器、主题系统及自定义布局。

注：项目目前处于重度开发阶段，API 可能变更。