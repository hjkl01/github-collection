### [bytecodealliance wasmtime](https://github.com/bytecodealliance/wasmtime)  ![GitHub Repo stars](https://img.shields.io/github/stars/bytecodealliance/wasmtime?style=social)

Wasmtime 是由 Bytecode Alliance 开发的 WebAssembly 独立运行时，提供命令行工具及多种语言的库嵌入支持。

核心特性：
1. **高性能**：基于 Cranelift 优化代码生成，实现高效实例化、低开销调用及并发实例扩展。
2. **高安全**：基于 Rust 构建，经过严格审查与模糊测试，具备完善的安全策略及漏洞修复机制。
3. **可配置**：默认配置易用，同时支持精细控制 CPU 和内存消耗，适应不同环境规模。
4. **标准合规**：通过 WebAssembly 官方测试套件，实现 WASI 标准及 C API，支持 WebAssembly 未来提案。
5. **多语言支持**：官方支持 Rust、C、Python、.NET、Go、Ruby 等语言嵌入，社区支持其他语言。