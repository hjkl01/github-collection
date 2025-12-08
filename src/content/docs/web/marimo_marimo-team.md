
---
title: marimo
---

### [marimo-team marimo](https://github.com/marimo-team/marimo)

**marimo** 是一个可重复、交互式且可分享的 Python 编程环境，旨在替代传统笔记本的 JSON 草稿形式。其核心功能包括：  
1. **响应式编程**：代码与数据自动同步更新，支持动态交互。  
2. **多功能支持**：集成 SQL 单元、AI 代码补全、数据可视化及布局管理。  
3. **兼容性**：支持将 Jupyter 笔记本自动转换为 marimo 格式，并可通过命令行工具创建、编辑和运行应用。  
4. **灵活使用**：可作为脚本执行（`python your_notebook.py`），或通过 `marimo run` 以网页应用形式运行（隐藏代码）。  
5. **社区资源**：提供教程、示例及云服务（molab）支持协作与分享。  

**使用方法**：  
- 安装：`pip install marimo` 或 `conda install -c conda-forge marimo`。  
- 创建/编辑笔记本：`marimo edit`。  
- 运行应用：`marimo run your_notebook.py`。  
- 转换 Jupyter 笔记本：`marimo convert your_notebook.ipynb > your_notebook.py`。  

**主要特性**：交互式数据可视化、模块化布局、支持云协作、与主流 Python 生态（如 NumPy、SciPy）兼容。