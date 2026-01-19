
---
title: googletest
---

### [google googletest](https://github.com/google/googletest)  ![GitHub Repo stars](https://img.shields.io/github/stars/google/googletest?style=social)

**项目核心内容总结：**

**功能**：GoogleTest 是 Google 开发的 C++ 单元测试框架，合并了原 GoogleTest 和 GoogleMock 项目，支持单元测试及模拟对象测试。  

**使用方法**：  
- 通过 [官方文档](https://google.github.io/googletest/) 查阅指南，推荐从 [快速入门](https://google.github.io/googletest/primer.html) 开始。  
- 具体构建方法参见 `googletest/README.md`。  

**主要特性**：  
- 基于 xUnit 架构，支持自动测试发现、无需手动注册测试用例。  
- 提供丰富断言（如等值、异常检测），支持自定义断言。  
- 支持死亡测试（验证程序异常退出）、参数化测试（值参数化/类型参数化）。  
- 支持测试顺序控制、并行运行测试。  

**支持平台**：遵循 Google C++ 支持政策，兼容主流编译器、平台及构建工具（具体版本见 [支持矩阵](https://github.com/google/oss-policies-info/blob/main/foundational-cxx-support-matrix.md)）。  

**其他**：1.17.x 版本起要求 C++17 及以上。