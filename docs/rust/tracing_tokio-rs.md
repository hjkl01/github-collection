### [tokio-rs tracing](https://github.com/tokio-rs/tracing)  ![GitHub Repo stars](https://img.shields.io/github/stars/tokio-rs/tracing?style=social)

`tracing` 是一个用于对 Rust 程序进行插桩的框架，旨在收集结构化的、基于事件的应用级诊断信息，且不依赖 Tokio 运行时。它通过宏和属性（如 `#[instrument]`）记录跟踪事件与 Span，允许应用程序通过 `Subscriber` 接口收集数据，而库仅需插桩无需安装订阅器。框架支持异步代码的准确追踪，并提供 `tracing-subscriber` 等核心扩展库及 OpenTelemetry 等第三方集成。