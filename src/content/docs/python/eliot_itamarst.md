
---
title: eliot
---

### [itamarst eliot](https://github.com/itamarst/eliot)  ![GitHub Repo stars](https://img.shields.io/github/stars/itamarst/eliot?style=social)

Eliot 是一个 Python 日志系统，通过输出动作的因果链来解释事件发生的原因，而非仅记录孤立事实。它帮助用户定位性能瓶颈、理解代码路径选择及排查错误。支持单机日志记录、分布式系统因果追踪，并内置对 NumPy、Dask、Asyncio、Trio 及 Twisted 的集成支持。日志生成后需配合外部工具进行聚合存储。兼容 Python 3.9 至 3.13 及 PyPy3。