
---
title: checkov
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/bridgecrewio/checkov?style=social) ](https://github.com/bridgecrewio/checkov)
### [bridgecrewio checkov](https://github.com/bridgecrewio/checkov)

**Checkov 项目核心内容总结：**

Checkov 是一个用于检测基础设施即代码（IaC）和容器镜像中安全和合规问题的静态分析工具。它支持多种格式的配置文件，如 Terraform、CloudFormation、Kubernetes、Dockerfile 等，并能够对代码进行扫描，识别潜在的漏洞和违规行为。

**主要功能：**
- 提供丰富的内置检查规则，覆盖安全、合规、最佳实践等多个方面；
- 支持多种 IaC 工具和文件格式；
- 提供详细的扫描结果，包括问题位置、检查 ID、修复建议等；
- 支持通过注释的方式对特定检查进行忽略或抑制；
- 支持通过配置文件自定义扫描行为，如忽略路径、检查规则、输出格式等；
- 可集成到 CI/CD 流程中，支持命令行和 VS Code 插件使用。

**使用方法：**
- 可通过命令行运行 Checkov，指定扫描目录、文件或镜像；
- 支持自定义配置文件，用于设置扫描参数；
- 提供多种输出格式，如 CLI、JSON、HTML 等；
- 支持与 Prisma Cloud 平台集成，获取更多修复指南。

**主要特性：**
- 支持多语言和多格式的 IaC 工具；
- 提供详细的检查规则和修复建议；
- 支持忽略检查、自定义规则和配置；
- 支持集成到开发工具链（如 VS Code）；
- 支持通过 API 获取修复指南（可选择跳过）；
- 支持 Python 3.9 至 3.13 版本。

**使用注意事项：**
- 使用前请确保安装 Python 并满足版本要求；
- 检查结果可通过注释或配置文件进行抑制；
- 可通过 `--skip-download` 选项跳过 API 请求；
- 默认会忽略一些目录（如 `.terraform`、`node_modules` 等），可通过配置调整。