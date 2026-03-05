
---
title: marimo
---

### [marimo-team marimo](https://github.com/marimo-team/marimo)  ![GitHub Repo stars](https://img.shields.io/github/stars/marimo-team/marimo?style=social)

marimo 是一个响应式 Python 笔记本，兼具脚本的可重现性和应用的可部署性，旨在替代 Jupyter 和 Streamlit 等工具。

核心功能如下：
- **响应式执行**：运行单元格或修改 UI 元素时，自动执行依赖项，确保代码、输出和程序状态一致，消除隐藏状态。
- **Git 友好与脚本化**：笔记本存储为纯 Python 文件，支持版本控制，可直接作为 Python 脚本执行或通过 CLI 运行。
- **交互与部署**：支持滑块、表格等 UI 元素与 Python 变量绑定，无需回调代码，可一键部署为交互式 Web 应用或幻灯片。
- **数据与 AI 支持**：内置 SQL 引擎，支持查询数据框、数据库等；支持 AI 生成代码和单元格，具备内置包管理。
- **开发体验**：支持单元测试（pytest）、确定性执行顺序，兼容 VS Code、Neovim 等主流编辑器。