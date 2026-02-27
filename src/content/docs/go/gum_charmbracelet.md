
---
title: gum
---

### [charmbracelet gum](https://github.com/charmbracelet/gum)  ![GitHub Repo stars](https://img.shields.io/github/stars/charmbracelet/gum?style=social)

Gum 是一个用于美化 shell 脚本的工具，它允许用户在不编写任何 Go 代码的情况下，利用 Bubbles 和 Lip Gloss 的功能。Gum 提供了多种实用命令，用于创建交互式脚本，如选择、确认、输入、过滤、格式化、表格显示等。

**核心功能：**

- **交互式命令**：提供 `choose`（选择）、`confirm`（确认）、`input`（输入）、`filter`（过滤）、`write`（多行输入）、`file`（文件选择）、`spin`（加载动画）、`table`（表格）、`style`（样式）、`join`（拼接）、`format`（格式化）、`log`（日志）等命令。
- **样式定制**：支持通过命令行参数或环境变量自定义颜色、边框、对齐方式等。
- **跨平台支持**：支持 Linux、macOS、Windows、FreeBSD、OpenBSD、NetBSD 等系统。
- **安装便捷**：支持通过 Homebrew、APT、YUM、Nix、Scoop、WinGet 等多种方式安装，也可通过 Go 安装。
- **脚本示例**：提供多种实际使用场景的脚本示例，如 Git 提交、文件管理、tmux 会话切换等。

**使用方法：**

Gum 的每个命令都可以通过命令行调用，并支持多种参数进行定制。例如：

- `gum choose "选项1" "选项2"`：从多个选项中选择一个。
- `gum input --placeholder "提示"`：提示用户输入。
- `gum confirm`：确认操作。
- `gum filter < 文件`：从文件中模糊搜索。
- `gum style`：对文本进行样式设置。
- `gum log`：记录带级别的日志信息。

**主要特性：**

- **美观界面**：提供丰富的样式和布局选项，使脚本交互更友好。
- **高度可定制**：支持通过参数或环境变量自定义外观。
- **简单易用**：命令简单直观，适合快速集成到 shell 脚本中。
- **跨平台兼容**：支持主流操作系统和多种安装方式。
- **丰富示例**：提供多个实际应用场景的示例脚本，方便用户直接使用或参考。