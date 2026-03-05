
---
title: diagram-as-code
---

### [awslabs diagram-as-code](https://github.com/awslabs/diagram-as-code)  ![GitHub Repo stars](https://img.shields.io/github/stars/awslabs/diagram-as-code?style=social)

awsdac 是一款通过 YAML 代码生成 AWS 基础设施架构图的命令行工具，实现了“图示即代码”（Diagram-as-code）。

**核心功能：**
- **代码化绘图**：无需图像库或 GUI 依赖，支持将架构图纳入 Git 版本控制，便于复用、测试、CI/CD 集成与自动化。
- **AWS 合规**：生成的图表符合 AWS 架构图标指南。
- **轻量灵活**：支持容器部署，自动调整资源位置与大小，智能处理连线。
- **集成与扩展**：支持作为 Golang 库调用，可从 CloudFormation 模板转换生成图示，且可扩展定义非 AWS 资源。

该工具旨在实现基础设施文档与实际代码的一致性，简化架构图的维护流程。