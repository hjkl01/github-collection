### [sirupsen logrus](https://github.com/sirupsen/logrus)  ![GitHub Repo stars](https://img.shields.io/github/stars/sirupsen/logrus?style=social)

Logrus 是一个 Go 语言的结构化日志库，完全兼容 Go 标准库日志接口。该项目处于维护模式，专注于安全性、Bug 修复和性能优化。核心功能包括：

1. **多种日志格式**：支持文本格式（TTY 环境支持彩色显示）和 JSON 格式（便于日志聚合分析）。
2. **多级日志**：提供 Trace 至 Panic 共七种日志级别，支持动态调整输出级别。
3. **结构化字段**：支持在日志中添加自定义字段，便于上下文追踪。
4. **钩子机制（Hooks）**：可扩展至 Syslog、异常追踪服务，支持多路日志输出。
5. **兼容性与集成**：可转换为 `io.Writer`，方便无缝替换或包装标准库日志。
6. **辅助功能**：默认线程安全，内置测试断言工具及 Fatal 级别退出处理器。