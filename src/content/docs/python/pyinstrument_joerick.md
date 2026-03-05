
---
title: pyinstrument
---

### [joerick pyinstrument](https://github.com/joerick/pyinstrument)  ![GitHub Repo stars](https://img.shields.io/github/stars/joerick/pyinstrument?style=social)

pyinstrument 是一款 Python 性能分析工具（Profiler），旨在帮助开发者定位程序中的性能瓶颈，从而优化代码速度。

主要功能包括：
1. **多方式调用**：支持命令行执行、Python 上下文管理器、装饰器及 Jupyter/IPython 集成。
2. **多样化报告**：提供终端文本、交互式 HTML（含时间线视图）、JSON、pstats 及 Speedscope 格式输出。
3. **框架与异步支持**：内置 Django、FastAPI 等框架中间件，原生支持 async/await 异步代码分析。
4. **高级分析**：自动识别并隐藏第三方库代码，支持性能分析会话的保存与加载，兼容 Python 3.8+。