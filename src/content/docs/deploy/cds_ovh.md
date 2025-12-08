
---
title: cds
---

### [ovh cds](https://github.com/ovh/cds)

**项目核心内容总结：**

**功能：**  
CDS 是一个基于 Go 语言开发的企业级持续交付（CI/CD）和 DevOps 自动化平台，支持从代码构建、测试、部署到运维的全生命周期管理。提供可视化界面（UI）和命令行工具（cdsctl），支持工作流（Workflow）和流水线（Pipeline）的创建与执行，可集成多种云平台和开发工具。

**使用方法：**  
- 通过 Docker-Compose 或二进制文件快速部署。  
- 使用 `cdsctl` 命令行工具实现工作流创建、执行、监控等功能，支持跨平台（Linux、Windows、macOS 等）。  
- 通过 Git 仓库配置实现“工作流即代码”，支持 YAML 文件定义流程，并可在 UI 中直接编辑。  

**主要特性：**  
1. **灵活的工作流管理**：支持多环境（开发/测试/生产）、权限控制（ACL）、自定义执行环境（Docker/VM/本地进程）。  
2. **高可用与扩展性**：无状态设计，支持水平扩展、多云自动扩缩容（Kubernetes/OpenStack/VMware 等）。  
3. **多租户与隔离**：用户可自建项目、工作流模板、执行模型，实现资源隔离与权限分级。  
4. **集成能力**：支持 GitHub/GitLab 等版本控制、Kubernetes/OpenStack 等云平台、Prometheus 等监控系统。  
5. **自动化与监控**：提供 REST API 和 SDK，支持自定义插件；内置指标监控，兼容 Prometheus 等工具。  
6. **安全与协作**：支持敏感信息加密、角色权限分配、审计日志，确保部署安全。  

**许可证**：3-clause BSD。