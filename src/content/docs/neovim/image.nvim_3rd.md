
---
title: image.nvim
---

### [3rd image.nvim](https://github.com/3rd/image.nvim)  ![GitHub Repo stars](https://img.shields.io/github/stars/3rd/image.nvim?style=social)

### 项目简介：image.nvim

**image.nvim** 是一个为 Neovim 提供图片渲染支持的插件，利用 [Kitty 的图形协议](https://sw.kovidgoyal.net/kitty/graphics-protocol/) 或 [ueberzugpp](https://github.com/jstkdng/ueberzugpp) 实现。支持在 Markdown、Neorg、Asciidoc、RST、Typst、HTML 等文档中嵌入并显示图片，特别适合在终端中工作时查看图像内容。

---

### 项目功能

- **支持多种渲染后端**：
  - **Kitty（推荐）**：性能最佳，支持原生裁剪、缓存等。
  - **ueberzugpp**：兼容所有终端，但性能较低。
  - **Sixel**：适用于支持 Sixel 协议的终端（如 XTerm、WezTerm），性能一般。

- **支持多种文档格式**：
  - Markdown（含 VimWiki、Quarto）
  - Asciidoc
  - Neorg
  - RST
  - Typst
  - HTML、CSS（可选）

- **智能渲染特性**：
  - 支持仅在光标所在位置渲染图片（`only_render_image_at_cursor`）
  - 支持浮动窗口渲染图片
  - 支持远程图片下载和渲染
  - 支持 Tmux 环境下的渲染（需配置 Tmux）

- **自定义配置**：
  - 图片最大尺寸、缩放比例、窗口占比等
  - 每种文档格式可单独配置
  - 支持自定义图片路径解析函数

- **API 接口**：
  - 通过 Lua API 可实现图片的加载、渲染、移动、调整亮度/饱和度/色相等
  - 支持从本地文件或远程 URL 加载图片

---

### 使用方法

1. **安装依赖**：
   - 安装 Kitty（推荐）或 ueberzugpp 或支持 Sixel 的终端
   - 安装 [ImageMagick](https://imagemagick.org/)（用于图片处理）
   - 安装 LuaRock（如使用 `magick_rock` 处理器）

2. **安装插件**：
   - 使用 Lazy 或其他插件管理器安装 `image.nvim`

3. **配置插件**：
   - 设置渲染后端（如 `backend = "kitty"`）
   - 设置图片处理器（如 `processor = "magick_cli"`）
   - 启用文档格式的图片支持（如 Markdown、Neorg 等）
   - 可配置最大尺寸、缩放、仅渲染光标所在图片等选项

4. **快速测试**：
   - 下载 [minimal-setup.lua](./minimal-setup.lua) 并运行 `nvim --clean -c ":luafile minimal-setup.lua"` 快速体验

---

### 主要特性

- **支持 Tmux**：在 Tmux 中也能正常渲染图片
- **性能优化**：Kitty 后端性能最佳，支持缓存和裁剪
- **多终端兼容**：ueberzugpp 和 Sixel 支持广泛终端
- **文档集成**：支持 Markdown、Neorg 等文档格式中的图片嵌入
- **API 强大**：可编程控制图片的显示、移动、样式等
- **可扩展性强**：支持自定义图片路径解析、文档格式扩展等