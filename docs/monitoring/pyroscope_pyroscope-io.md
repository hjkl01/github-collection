### [pyroscope-io pyroscope](https://github.com/pyroscope-io/pyroscope)  ![GitHub Repo stars](https://img.shields.io/github/stars/pyroscope-io/pyroscope?style=social)

Grafana Pyroscope 是一个连续性能剖析平台，用于从应用程序中揭示性能洞察，帮助优化 CPU、内存及 I/O 等资源消耗。它支持主动预防性能问题和被动排查系统瓶颈，提供行级别的调试细节以辅助根因分析。

系统主要由三个核心组件构成：
1. **Pyroscope Server**：负责存储和处理剖析数据。
2. **数据采集端**：通过 Pyroscope SDKs 或 Grafana Alloy 从应用收集数据，支持 Go、Java、Python、Ruby、Node.js、.NET、Rust 及 eBPF 等多种语言和环境。
3. **Explore Profiles UI**：集成于 Grafana 的无查询直观界面，用于可视化和分析剖析数据。

该平台旨在帮助开发者全面理解应用行为，并在生产环境中进行针对性的性能优化与故障解决。