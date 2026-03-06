
---
title: pdoc
---

### [mitmproxy pdoc](https://github.com/mitmproxy/pdoc)  ![GitHub Repo stars](https://img.shields.io/github/stars/mitmproxy/pdoc?style=social)

pdoc 是一款 Python API 文档生成工具，专注于简洁易用，可将 Python 项目转换为独立的 HTML 文档。

核心功能：
*   **文档支持**：支持 Markdown 语法，兼容 numpydoc 和 Google 风格 docstring。
*   **代码解析**：全面支持类型注解、AST 遍历提取，自动解析前向引用及继承关系。
*   **交互体验**：内置 Web 服务器，支持实时重载预览。
*   **输出定制**：可自定义 HTML 模板，输出无依赖的静态站点。
*   **标识符处理**：自动链接 docstring 中的标识符，尊重 `__all__` 变量。

适用于常规 Python 项目文档生成，复杂需求推荐使用 Sphinx。