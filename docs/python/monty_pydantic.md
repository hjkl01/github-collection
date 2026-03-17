### [pydantic monty](https://github.com/pydantic/monty)  ![GitHub Repo stars](https://img.shields.io/github/stars/pydantic/monty?style=social)

Monty 是用 Rust 编写的极简安全 Python 解释器，面向 AI 代理执行 LLM 生成代码。它以微秒级启动、接近 CPython 的运行性能，支持有限的 Python 语法和少量标准库；可严格隔离主机环境，所有文件、网络、环境变量访问需由开发者提供外部函数；支持调用指定宿主函数、类型检查、资源限制、收集 stdout/stderr；可在外部函数调用处快照/序列化并恢复执行；可从 Rust、Python、JavaScript 调用，支持同步/异步执行。用途是替代容器沙箱，安全运行代理代码。