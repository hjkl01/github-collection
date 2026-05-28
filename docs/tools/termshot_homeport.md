### [termshot](https://github.com/homeport/termshot) ![GitHub Repo stars](https://img.shields.io/github/stars/homeport/termshot?style=social)

termshot 是一个命令行工具，用于“在终端里给终端输出截图”。它通过读取命令输出中的 ANSI 转义序列来高保真渲染终端内容，并生成类似窗口界面的图片（默认 `out.png`），而不是仅对纯文本做语法高亮。

核心功能包括：
- 给任意命令输出生成终端截图（如 `termshot ls -a`）。
- 支持复杂命令（含管道）与交互式场景（可启动完整 shell，结束后统一截图）。
- 可控制截图样式：是否显示命令、列宽换行、窗口装饰、阴影、外边距、内边距等。
- 可控制输出方式：自定义文件名/路径，或在支持的平台直接复制到系统剪贴板。
- 支持截图前编辑输出内容（通过 `$EDITOR`，默认回退 `vi`），便于删除敏感信息。
- 支持原始数据读写：
  - `--raw-write`：仅保存原始命令输出，不生成截图；
  - `--raw-read`：从文件读取输入并生成截图，不执行命令。
- 提供版本查看等常用参数。

安装方式支持 Homebrew（macOS/Linux），并提供 Darwin 与 Linux 的预编译发布包。项目仍在持续开发中，部分 ANSI 序列和光标重置类输出可能暂未完全兼容。