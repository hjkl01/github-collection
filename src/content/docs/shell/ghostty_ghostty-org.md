
---
title: ghostty
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/ghostty-org/ghostty?style=social) ](https://github.com/ghostty-org/ghostty)
### [ghostty-org ghostty](https://github.com/ghostty-org/ghostty)

**项目核心内容总结：**

Ghostty 是一款功能丰富、速度快且原生的终端模拟器，支持跨平台使用（Mac、Linux、Windows）。其核心特性包括：
1. **标准兼容性**：严格遵循终端标准（如 ECMA-48）及主流终端（如 xterm）行为，确保与现有工具兼容。
2. **高性能**：采用 Metal（Mac）和 OpenGL（Linux）渲染技术，支持高帧率（60fps）及高效 IO 处理。
3. **原生体验**：Mac 端基于 SwiftUI 实现完整菜单栏和设置界面，Linux 端使用 GTK。
4. **窗口功能**：支持多窗口、标签页、分屏操作。
5. **可嵌入库**：提供 `libghostty` 库，允许第三方应用集成终端功能（目前支持 Zig/C 语言）。

**使用方法：**
- 下载地址：[ghostty.org/download](https://ghostty.org/download)
- 文档：[ghostty.org/docs](https://ghostty.org/docs)
- 贡献方式：阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 和 [HACKING.md](HACKING.md) 文件。

**其他：**
- 支持崩溃报告生成（保存路径：`$XDG_STATE_HOME/ghostty/crash`），可通过 Sentry CLI 上传至项目团队。