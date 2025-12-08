
---
title: insomnia
---

### [Kong insomnia](https://github.com/Kong/insomnia)

**Insomnia API 客户端核心内容总结：**  

**项目功能：**  
Insomnia 是一款开源、跨平台的 API 客户端，支持 GraphQL、REST、WebSocket、Server-Sent Events（SSE）、gRPC 等多种协议。主要功能包括：  
- 调试 API（支持主流协议和格式）；  
- 设计 API（内置 OpenAPI 编辑器和可视化预览）；  
- 测试 API（支持测试套件和集合运行器）；  
- 模拟 API（云端或自托管模拟服务器）；  
- 构建 CI/CD 管道（通过 Insomnia CLI 实现代码检查和测试）；  
- 协作功能（支持团队协作）。  

**使用方法：**  
- 通过 [https://insomnia.rest](https://insomnia.rest) 下载适用于 Mac、Windows 和 Linux 的客户端；  
- 免费使用需注册账户，但可选择本地存储（Local Vault）以完全本地保存项目数据，无需依赖云端；  
- 通过 Git Sync 或 Cloud Sync 实现团队协作，Cloud Sync 支持端到端加密（E2EE）。  

**主要特性：**  
- **存储灵活**：支持本地、Git 和云端存储，数据存储方式可自定义；  
- **安全隐私**：Private Environments 功能确保环境配置始终本地存储，不上传云端；  
- **协作与扩展**：支持无限协作、Git 同步、组织管理、第三方登录（SAML/OIDC）等高级功能（需订阅）；  
- **开源与插件**：支持第三方插件扩展（如文档生成、GitHub API 导入等），社区提供丰富工具（如 Insomnia Documenter）。  

**许可证**：Apache-2.0 开源协议。