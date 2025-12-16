
---
title: PrettyErrors
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/onelivesleft/PrettyErrors?style=social) ](https://github.com/onelivesleft/PrettyErrors)
### [onelivesleft PrettyErrors](https://github.com/onelivesleft/PrettyErrors)

**核心内容总结：**

`pretty_errors` 是一个用于美化 Python 异常输出的库，使错误信息更易读。主要功能包括：

1. **使用方法**  
   - 安装：`python -m pip install pretty_errors`  
   - 全局启用：运行 `python -m pretty_errors`，使所有脚本的异常输出自动美化。  
   - 项目内使用：直接导入 `import pretty_errors`，但需在支持颜色的终端（如 Windows 的 PowerShell）中使用，否则需调用 `pretty_errors.mono()` 开启黑白模式。

2. **主要特性**  
   - **高度可配置**：通过 `configure()` 方法自定义分隔符、显示行数、颜色、文件路径显示方式等。  
   - **黑白名单控制**：使用 `whitelist()` 和 `blacklist()` 设置需显示或排除的路径。  
   - **路径化配置**：为不同路径设置独立的显示规则（如系统路径使用灰色显示）。  
   - **环境变量控制**：通过 `PYTHON_PRETTY_ERRORS` 禁用库，或 `PYTHON_PRETTY_ERRORS_ISATTY_ONLY` 限制其仅在交互式终端生效。  
   - **异常信息增强**：支持显示局部变量、代码上下文、语法错误箭头提示等。  
   - **兼容性处理**：提供 `replace_stderr()` 替代 `sys.excepthook`，解决部分框架（如 `uvicorn`）冲突问题。  

3. **配置选项**  
   - 包括颜色设置（如 `line_color`、`filename_color`）、显示格式（如 `lines_before`、`display_locals`）、路径规则等，支持通过 `pretty_errors.default_config` 查看默认值并自定义。  

4. **高级定制**  
   - 可通过继承 `ExceptionWriter` 类覆盖 `write_` 方法，实现完全自定义的输出格式。