
---
title: cli
---

### [cli cli](https://github.com/cli/cli)

### 核心内容总结

**项目功能**  
GitHub CLI（`gh`）是一款命令行工具，将 GitHub 的拉取请求、问题等核心功能集成到终端，与 `git` 和代码开发环境无缝结合，提升开发者在终端处理 GitHub 任务的效率。

**使用方法**  
支持多种安装方式：  
- **macOS**：通过 Homebrew 或预编译二进制文件安装；  
- **Linux/Unix**：支持 Debian、RPM 等系统包，或预编译二进制文件；  
- **Windows**：支持 WinGet 或预编译二进制文件；  
- **从源码构建**：提供详细构建说明；  
- **GitHub Codespaces**：通过配置 devcontainer 文件集成；  
- **GitHub Actions**：托管运行器已预装 `gh`，支持指定版本安装。

**主要特性**  
- 兼容 GitHub.com、GitHub Enterprise Cloud 和 GitHub Enterprise Server 2.20+；  
- 支持跨平台（macOS、Windows、Linux）；  
- 提供**二进制文件验证功能**，使用 Sigstore 的 `cosign` 实现加密验证，确保下载文件的来源可信；  
- 与 `hub` 工具相比，`gh` 是独立的官方工具，设计更现代，功能更全面。