### [itamarst eliot](https://github.com/itamarst/eliot)  ![GitHub Repo stars](https://img.shields.io/github/stars/itamarst/eliot?style=social)

Eliot 是一款 Python 日志系统，通过输出行动的因果链来解释应用程序中事件发生的“原因”，而非仅仅记录事实。它支持行动相互生成及最终成功或失败的追踪，有助于定位性能瓶颈、理解代码路径选择及排查错误。适用于单机日志、分布式系统因果追踪、科学计算（内置 NumPy 和 Dask 支持）以及异步/网络框架（Asyncio、Trio、Twisted）。兼容 Python 3.9-3.13 及 PyPy3。