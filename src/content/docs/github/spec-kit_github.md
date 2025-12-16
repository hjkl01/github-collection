
---
title: spec-kit
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/github/spec-kit?style=social) ](https://github.com/github/spec-kit)
### [github spec-kit](https://github.com/github/spec-kit)

**核心内容总结：**

**项目功能**  
Spec-Kit 是一个基于“规范驱动开发”（Spec-Driven Development）的工具，通过 AI 代理（如 Claude Code）自动生成代码、技术计划、任务分解及测试方案，支持 .NET Aspire、PostgreSQL、Blazor 等技术栈，实现从需求到代码的自动化开发流程。

**使用方法**  
1. 初始化项目并配置 AI 代理；  
2. 生成功能规范（Spec）文件；  
3. 指定技术栈后生成技术计划（Plan）；  
4. 分解任务为可执行步骤（Tasks）；  
5. 执行代码实现（Implement）；  
6. 测试并修复运行时问题。

**主要特性**  
- 支持多技术栈（如 .NET、PostgreSQL、Blazor）；  
- 自动生成代码、API 规范、数据模型等文档；  
- 任务分解与依赖管理，标注并行执行任务；  
- 测试驱动开发（TDD）结构；  
- 集成 GitHub CLI，支持生成 Pull Request；  
- 遵循项目规范文件（Constitution）确保开发一致性。