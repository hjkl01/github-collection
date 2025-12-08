
---
title: act
---

### [nektos act](https://github.com/nektos/act)

**项目核心内容总结：**  
`act` 是一个用于本地运行 GitHub Actions 的工具，支持在开发阶段直接测试工作流文件（`.github/workflows/`）和嵌入式 GitHub Actions，无需提交代码。其核心功能包括：  
1. **快速反馈**：模拟 GitHub 的环境变量和文件系统，提供与 GitHub 宿主环境一致的运行环境。  
2. **本地任务运行**：替代 `Makefile`，通过 GitHub Actions 定义的流程执行任务。  
3. **Docker 支持**：自动拉取或构建 Docker 镜像，按依赖关系执行容器化任务。  

**使用方法**：  
- 安装 Go 1.20+ 后，通过 `git clone` 获取源码并使用 `make install` 安装。  
- 直接运行 `act` 命令执行工作流，或通过 VS Code 扩展（[GitHub Local Actions](https://sanjulaganepola.github.io/github-local-actions-docs/)）集成使用。  

**主要特性**：  
- 完全兼容 GitHub 宿主运行器的环境配置。  
- 支持自定义工作流的调试与本地化测试。  
- 提供可视化调试工具（如 VS Code 插件）。