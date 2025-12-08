
---
title: boa
---

### [boa-dev boa](https://github.com/boa-dev/boa)

**核心内容总结：**  
Boa 是一个用 Rust 编写的 JavaScript 引擎，支持超过 90% 的 ECMAScript 规范，提供词法分析、解析和执行功能。主要特性包括：  
- **多组件支持**：包含 `boa_engine`（执行 JS 代码）、`boa_cli`（命令行工具）、`boa_parser`（解析器）等模块；  
- **使用方法**：通过 `Cargo.toml` 添加 `boa_engine` 依赖，示例代码展示如何执行 JS，如 `cargo run` 运行测试；  
- **功能扩展**：支持 WASM 在线演示、CLI 模式、AST 生成与调试、模块加载等；  
- **测试与基准**：提供 ECMAScript 测试套件结果、V8 基准测试对比及性能分析工具；  
- **贡献与协作**：支持通过 Matrix 和 Discord 参与讨论，采用 Unlicense 或 MIT 许可证。