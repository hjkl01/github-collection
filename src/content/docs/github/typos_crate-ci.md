
---
title: typos
---

### [crate-ci typos](https://github.com/crate-ci/typos)

**项目核心内容总结：**  
typos 是一款用于检测和修正源代码中拼写错误的工具，支持快速处理大型仓库，且误报率低，适合在代码提交中使用。  

**功能与使用方法：**  
- **安装方式**：支持通过 Cargo、Homebrew、Conda、Pacman 等安装，或直接下载预编译二进制文件。  
- **基本用法**：运行 `typos` 查看拼写错误，使用 `typos --write-changes` 自动修正（需确认无歧义）。  
- **自定义配置**：通过 `_typos.toml` 文件可添加忽略规则（如特定词汇、文件类型或路径），支持区分标识符和普通词汇的修正。  
- **集成支持**：提供 GitHub Action、pre-commit、Visual Studio Code 插件等集成方案，也可通过命令行参数（如 `--diff`、`--format json`）实现自定义调用。  

**主要特性：**  
- 专为代码拼写设计，区分标识符与普通词汇，减少误报。  
- 支持排除特定文件或目录（如本地化内容），仅检查文件名。  
- 提供调试工具（如 `--dump-config`、`--files` 等）辅助排查问题。  
- 可通过贡献修正规则扩展词库，提升准确性。