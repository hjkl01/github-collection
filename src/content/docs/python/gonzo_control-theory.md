
---
title: gonzo
---

### [control-theory gonzo](https://github.com/control-theory/gonzo)  ![GitHub Repo stars](https://img.shields.io/github/stars/control-theory/gonzo?style=social)

Gonzo 是一款基于 Go 开发的终端日志分析工具（TUI），核心功能总结如下：

1. **实时分析**：支持从文件、标准输入、网络流或 Kubernetes 集群实时读取和处理日志。
2. **交互式仪表盘**：采用类 k9s 的 2x2 网格布局，提供词频、严重性分布、热图等实时可视化图表。
3. **AI 智能洞察**：集成可配置的 AI 模型（如 GPT、Claude、本地模型），自动识别日志模式、异常并提供根因建议。
4. **高级过滤**：支持正则表达式、属性搜索、严重级别筛选及 Kubernetes 命名空间和 Pod 过滤。
5. **OTLP 原生支持**：内置 OpenTelemetry 日志格式解析器及 gRPC/HTTP OTLP 接收器。
6. **高度可定制**：提供多种内置主题，支持通过 YAML 自定义颜色和日志格式。
7. **易用交互**：兼容 Vim 风格快捷键及鼠标操作，支持全屏日志查看、暂停控制及 AI 聊天模式。