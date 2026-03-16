### [joerick pyinstrument](https://github.com/joerick/pyinstrument)  ![GitHub Repo stars](https://img.shields.io/github/stars/joerick/pyinstrument?style=social)

Pyinstrument 是一个 Python 性能分析（Profiler）工具，旨在帮助开发者优化代码性能，快速定位程序中最慢的部分。

**核心功能：**

*   **多模式分析**：支持命令行运行、Python 上下文管理器（with 块）、函数装饰器以及 Jupyter/IPython 集成，能够同时分析同步与异步（async/await）代码。
*   **多样化输出**：提供终端文本、交互式 HTML（含时间线模式、缩放与树形导航）、JSON、Speedscope 火焰图及 pstats 文件等多种报告格式。
*   **灵活配置**：支持自定义采样间隔、过滤特定路径或库代码、保存/加载分析会话，并提供 Django、FastAPI、aiohttp 等框架的中间件集成。
*   **广泛兼容**：支持 Python 3.8 及以上版本，包括最新的 3.11/3.12/3.13 版本。