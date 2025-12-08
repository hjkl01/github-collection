
---
title: terraform-provider-azurerm
---

### [hashicorp terraform-provider-azurerm](https://github.com/hashicorp/terraform-provider-azurerm)

**核心内容总结：**  
该项目是 Terraform 用于 Azure Resource Manager 的提供者，支持通过 Terraform 管理 Azure 资源。  

**功能与使用方法：**  
- **资源管理**：可创建资源组、虚拟网络等 Azure 资源，示例中通过 HCL 配置资源组和虚拟网络的名称、位置及网络地址空间。  
- **版本兼容性**：使用 4.0 版本时需搭配最新 Terraform 核心版本。  
- **认证方式**：支持 Azure CLI、托管身份及服务主体认证。  
- **特性配置**：通过 `features {}` 块可调整提供者行为。  

**主要特性：**  
- 提供详细文档和示例（如 GitHub 示例库）。  
- 支持通过 `required_providers` 指定提供者版本。  
- 开发者可参考 `DEVELOPER.md` 和 `contributing` 目录参与贡献。