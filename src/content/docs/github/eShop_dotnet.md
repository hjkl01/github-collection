
---
title: eShop
---

### [dotnet eShop](https://github.com/dotnet/eShop)

**核心内容总结：**

**项目功能**  
eShop 是一个基于 .NET Aspire 的电商网站参考应用，采用服务架构设计，用于演示如何使用 .NET 9 构建可扩展的电商系统，包含商品管理、用户交互等核心功能。

**使用方法**  
1. **环境准备**  
   - 克隆仓库并安装 Docker。  
   - Windows 用户可选 Visual Studio 2022（需安装 ASP.NET、.NET Aspire SDK 等组件）或通过 PowerShell 脚本自动配置环境。  
   - Mac/Linux 用户需安装 .NET 9 SDK 或 Visual Studio Code 及相关扩展。  

2. **运行项目**  
   - Visual Studio：打开 `eShop.Web.slnf`，设置 `eShop.AppHost.csproj` 为启动项目，按 Ctrl+F5 运行。  
   - 命令行：执行 `dotnet run --project src/eShop.AppHost/eShop.AppHost.csproj`，通过输出的 URL 访问 Aspire 控制台。  

3. **Azure 部署**  
   - 使用 Azure Developer CLI（azd）初始化项目，执行 `azd up` 部署至 Azure，支持通过 WebApp URL 访问应用。

**主要特性**  
- 基于 .NET 9 的服务架构，支持模块化开发。  
- 集成 Docker 容器化部署，支持多平台（Windows、Mac、Linux）。  
- 支持 Azure Open AI（需配置密钥和端点）。  
- 提供 Azure 快速部署方案，通过 azd 实现一键部署。  
- 包含虚构的示例数据（商品信息由 AI 生成）。