
---
title: swc
---

### [swc-project swc](https://github.com/swc-project/swc)

**核心内容总结：**  
SWC（Speedy Web Compiler）是一个用Rust编写的高性能TypeScript/JavaScript编译器，同时支持Rust和JavaScript生态。其核心功能包括快速编译、代码转换及优化，适用于前端开发场景。  

**使用方法：**  
- **Rust用户**：通过[官方文档](https://rustdoc.swc.rs/swc/)查阅API，使用`swc_ecma_parser`作为入口。  
- **JavaScript用户**：参考[官网安装指南](https://swc.rs/docs/installation/)集成。  
- 支持Node.js v10+运行，开发需Node.js v20+。  

**主要特性：**  
1. **高性能**：相比Babel，编译速度更快（详见[性能基准](https://swc.rs/docs/benchmark-transform)）。  
2. **兼容性**：支持最新Rust版本（MSRV 1.73），提供依赖更新脚本（需`jq`和`cargo upgrade`）。  
3. **跨语言支持**：同时作为Rust库和JavaScript工具链的一部分。  
4. **开源协议**：采用Apache License 2.0授权。