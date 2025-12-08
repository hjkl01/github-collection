
---
title: azure-sdk-for-python
---

### [Azure azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python)

**核心内容总结：**  
Azure SDK for Python 是微软提供的 Azure 云服务 Python 开发工具包，支持通过客户端库和管理库与 Azure 服务交互。  

**功能与使用方法：**  
- **客户端库**：提供对 Azure 服务的直接操作（如上传 Blob），分为新版本（遵循统一设计规范）和旧版本（功能稳定但可能不完整）。新版本依赖 `azure-core` 库，包含重试、日志、认证等功能。  
- **管理库**：用于 Azure 资源的部署与管理，遵循 Azure SDK 设计指南，支持身份验证、HTTP 管道、错误处理等，部分库需通过迁移指南从旧版本升级。  
- **使用方式**：用户可从 `/sdk` 目录选择特定服务的库，参考对应 `README` 文件进行安装和调用。  

**主要特性：**  
- 支持 Python 3.9 及以上版本。  
- 提供遥测配置选项（默认启用，可通过自定义策略关闭）。  
- 安全问题可通过邮件提交至 MSRC。  
- 开源贡献需遵守 CLA 协议，遵循 Microsoft 开源行为准则。  

**文档与支持：**  
- 官方文档地址：[Azure SDK for Python](https://aka.ms/python-docs)。  
- 问题反馈可通过 GitHub Issues 或 StackOverflow（标签 `azure` 和 `python`）。