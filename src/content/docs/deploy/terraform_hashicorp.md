
---
title: terraform
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/hashicorp/terraform?style=social) ](https://github.com/hashicorp/terraform)
### [hashicorp terraform](https://github.com/hashicorp/terraform)

**Terraform 核心内容总结：**

**项目功能**  
Terraform 是用于安全高效地构建、更改和版本化基础设施的工具，支持现有及主流云服务提供商（如 AWS、Azure 等）及企业自定义解决方案。

**主要特性**  
1. **基础设施即代码**：通过配置文件定义基础设施，支持版本控制、共享和复用。  
2. **执行计划**：生成变更预览（执行计划），明确资源创建/销毁顺序，避免意外操作。  
3. **资源依赖图**：自动分析资源依赖关系，优化并行操作效率，提升部署速度。  
4. **变更自动化**：基于执行计划和资源图，实现复杂变更的自动化执行，减少人为错误。

**使用方法**  
- 通过 [Terraform 官网文档](https://developer.hashicorp.com/terraform/docs) 和 [HashiCorp 学习平台](https://learn.hashicorp.com/terraform) 的入门教程开始使用。  
- 依赖的插件（Provider）可从 [Terraform Registry](https://registry.terraform.io) 自动下载。  
- 开发者可通过 [贡献指南](.github/CONTRIBUTING.md) 参与核心代码改进，或通过 [Web Unified Docs 仓库](https://github.com/hashicorp/web-unified-docs) 贡献文档。  

**许可证**  
采用 [Business Source License 1.1](https://github.com/hashicorp/terraform/blob/main/LICENSE) 开源协议。