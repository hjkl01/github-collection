
---
title: glow
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/charmbracelet/glow?style=social) ](https://github.com/charmbracelet/glow)
### [charmbracelet glow](https://github.com/charmbracelet/glow)

**核心内容总结：**

**项目功能**  
Glow 是一个基于终端的 Markdown 阅读器，支持在 CLI 中高效渲染 Markdown 文件，提供美观的文本用户界面（TUI）和命令行接口（CLI）模式，可浏览本地文件、Git 仓库或通过网络获取的 Markdown 内容。

**使用方法**  
- **安装**：支持 macOS、Linux、Windows 等平台的包管理器安装（如 Homebrew、Scoop），或通过 Go 编译安装（`go install`），也可直接下载二进制文件。  
- **TUI 模式**：运行 `glow` 启动界面，自动搜索当前目录或 Git 仓库中的 Markdown 文件，支持键盘操作（如 `?` 查看快捷键）。  
- **CLI 模式**：通过命令读取文件（`glow README.md`）、标准输入（`echo "..." | glow -`）、GitHub/GitLab 仓库（`glow github.com/xxx/xxx`）或 HTTP 链接（`glow https://xxx.md`）。

**主要特性**  
- 支持字幕包装（`-w` 设置最大宽度）、分页显示（默认使用 `less -r`）。  
- 可自定义样式（`-s` 参数选择 `dark`/`light` 或 JSON 样式文件）。  
- 配置文件（`glow.yml`）支持持久化设置，如默认样式、分页器、显示行号等。  
- 兼容多种终端环境，提供高性能渲染和交互体验。