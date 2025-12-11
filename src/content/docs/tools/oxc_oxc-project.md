
---
title: oxc
---

### [oxc-project oxc](https://github.com/oxc-project/oxc)

**项目核心内容总结：**  
Oxc 是一个基于 Rust 的高性能 JavaScript 和 TypeScript 工具集，由 VoidZero 公司开发，旨在构建下一代 JavaScript 工具链。项目提供多个工具模块，包括代码检查（linter）、格式化（formatter）、解析器（parser）、转换器（transformer）、压缩器（minifier）和解析工具（resolver），每个工具均支持通过 npm 或 Rust crate 安装使用。  

**主要特性：**  
- **高性能**：使用 Rust 实现，强调执行效率和资源优化；  
- **模块化**：工具可独立使用或组合集成，适应不同开发需求；  
- **广泛兼容**：被 Rolldown、Nuxt 等主流项目采用，被 Preact、Shopify 等公司使用；  
- **开发者友好**：提供详细的文档、在线 Playground 以及活跃的 Discord 社区支持。  

**使用方法：**  
- 通过 npm 安装各工具模块（如 `@oxc/linter`）；  
- 或使用 Rust crate（如 `oxc_parser`）集成到项目中；  
- 可直接访问在线 Playground 测试功能。  

**许可证：** 采用开源协议（如 MIT 或 Apache），支持商业和开源项目使用。