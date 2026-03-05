
---
title: checkov
---

### [bridgecrewio checkov](https://github.com/bridgecrewio/checkov)  ![GitHub Repo stars](https://img.shields.io/github/stars/bridgecrewio/checkov?style=social)

Checkov 是一款由 Prisma Cloud 维护的静态代码分析工具，用于基础设施即代码 (IaC) 安全合规扫描及软件成分分析 (SCA)。

**核心功能：**
1.  **多格式支持**：扫描 Terraform、Kubernetes、Dockerfile、CloudFormation、Helm 等多种 IaC 模板及 CI/CD 工作流文件。
2.  **漏洞与合规检测**：内置超 1000 条策略，检测云资源配置错误、敏感凭据泄露及开源组件漏洞 (CVE)。
3.  **高级分析**：支持基于图的上下文感知扫描、策略抑制、变量评估及自定义策略。
4.  **输出与集成**：支持 CLI、Docker 及 VS Code 扩展，提供 JSON、SARIF、JUnit XML 等多种输出格式。