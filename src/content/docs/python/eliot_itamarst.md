
---
title: eliot
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/itamarst/eliot?style=social) ](https://github.com/itamarst/eliot)
### [itamarst eliot](https://github.com/itamarst/eliot)

Eliot 是一个 Python 日志系统，通过输出 **因果链日志** 帮助开发者追踪软件行为的完整过程。其核心功能是记录代码执行的因果关系：每个操作（Action）可生成子操作，并最终标记为成功或失败，从而清晰呈现事件发生的原因和上下文。

**主要特性**：
1. 支持单进程日志、分布式系统追踪、科学计算（集成 NumPy 和 Dask）、异步编程（Asyncio/Trio）及 Twisted 网络框架。
2. 生成的日志能回答“为何发生错误”“性能瓶颈在哪”等问题，提供完整的操作链路追踪。
3. 兼容 Python 3.9-3.13 及 PyPy3，采用 Apache 2.0 许可证。

**使用方法**：
- 安装方式：通过 PyPI 或 conda-forge 安装。
- 需配合 Logstash、ElasticSearch 等工具处理多进程/分布式日志。
- 适用于需要精准追踪复杂流程的场景（如错误排查、性能分析）。

**其他信息**：
- 由 Itamar Turner-Trauring 维护，提供商业支持服务。
- 官方文档提供详细使用示例和集成指南。