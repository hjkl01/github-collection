
---
title: ginkgo
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/onsi/ginkgo?style=social) ](https://github.com/onsi/ginkgo)
### [onsi ginkgo](https://github.com/onsi/ginkgo)

**核心内容总结：**  
Ginkgo 是一个用于 Go 语言的成熟测试框架，支持行为驱动开发（BDD），通过与 Gomega 匹配器库结合，提供清晰的测试表达方式。其主要功能包括：  
1. **测试组织**：使用 `Describe`、`Context`、`When` 等容器节点嵌套组织测试用例，支持 `BeforeEach`/`AfterEach` 预置清理逻辑，`It`/`Specify` 定义测试主体。  
2. **运行特性**：支持测试随机化执行、并行化（通过 `ginkgo -p` 实现），自动中断超时测试，并提供上下文管理（`context.Context`）确保资源清理。  
3. **过滤与报告**：通过标签（Labels）过滤测试用例，支持命令行或代码中指定运行子集；生成多种格式的机器可读报告，支持自定义报告系统。  
4. **集成工具**：内置 `ginkgo` 命令行工具，支持生成、运行、过滤测试套件，及实时监控（`ginkgo watch`）实现快速反馈。  
5. **断言支持**：集成 Gomega，提供丰富的断言和匹配器，支持同步/异步测试，可扩展自定义匹配器。  

**使用方法**：通过 `ginkgo bootstrap` 初始化测试套件，使用 `ginkgo` 运行测试，`-p` 参数启用并行执行，通过标签或命令行过滤测试用例。  
**许可证**：MIT 协议。