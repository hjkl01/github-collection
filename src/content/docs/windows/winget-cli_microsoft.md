
---
title: winget-cli
---

### [microsoft winget-cli](https://github.com/microsoft/winget-cli)

**核心内容总结：**  

**项目功能**  
Windows Package Manager（WinGet）是一款用于快速发现和安装软件包的工具，支持通过命令行安装应用（如 `winget install <package>`），包来源包括 Microsoft Store（msstore）和社区仓库（winget）。  

**使用方法**  
1. **安装**：推荐通过 Microsoft Store 安装；也可手动下载开发版或自行构建客户端。  
2. **更新**：支持通过 Insider 程序获取开发版更新，或从 GitHub 发布页下载。  
3. **管理**：使用 `winget` 命令管理包，如安装、卸载、搜索等。  

**主要特性**  
- 支持多来源（官方商店、社区仓库、自定义 REST 源）。  
- 需管理员权限安装部分应用，否则可能因权限不足失败。  
- 提供实验性功能（需通过 `winget features` 启用）。  
- 自行构建客户端时需注意：无官方支持，需自行处理依赖（如 VC++ 运行库）。  
- 包含数据收集功能（可于系统设置中关闭）。  

**注意事项**  
- Windows Server 2019 不支持，Windows Server 2022 需手动安装依赖。  
- 非官方渠道安装需谨慎，可能影响自动更新。