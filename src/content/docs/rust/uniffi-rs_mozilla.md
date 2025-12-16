
---
title: uniffi-rs
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/mozilla/uniffi-rs?style=social) ](https://github.com/mozilla/uniffi-rs)
### [mozilla uniffi-rs](https://github.com/mozilla/uniffi-rs)

**核心内容总结：**  
UniFFI 是一个为 Rust 生成多语言绑定的工具，用于构建跨平台软件组件。用户可将核心逻辑用 Rust 实现，并通过接口定义文件（UDL）或 proc-macro 描述接口模型，UniFFI 会自动生成目标语言的绑定代码。支持的语言包括 Kotlin、Swift、Python、Ruby，第三方还支持 C#、Go、Dart、Java 等。主要特性包括：  
1. **跨平台共享库**：将 Rust 代码编译为共享库，供不同平台使用；  
2. **多语言绑定生成**：自动生成 Kotlin、Swift 等语言的调用接口；  
3. **灵活的接口定义**：支持 UDL 文件或宏定义接口模型；  
4. **社区生态**：提供第三方插件（如 Kotlin 多平台支持、IDEA 语法高亮工具）及构建工具（如 cargo-swift、Android Gradle 插件）。  

**使用方法**：  
- 编写 Rust 核心逻辑；  
- 通过 UDL 文件或 proc-macro 定义接口；  
- 使用 UniFFI 工具生成目标语言的绑定代码，并编译为共享库；  
- 在目标语言项目中调用生成的绑定。  

**主要特性**：  
- 支持多语言绑定生成；  
- 提供用户指南与示例；  
- 社区活跃，有第三方工具和资源扩展支持。