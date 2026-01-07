
---
title: pixi
---

### [prefix-dev pixi](https://github.com/prefix-dev/pixi)  ![GitHub Repo stars](https://img.shields.io/github/stars/prefix-dev/pixi?style=social)

**核心内容总结：**  
Pixi 是一个基于 Conda 生态系统的跨平台多语言包管理工具，支持 Python、C++、R 等多种语言，提供环境管理、任务运行和依赖管理功能。其主要特性包括：  
1. **跨平台兼容**：支持 Linux、Windows 等主流操作系统。  
2. **锁文件机制**：确保依赖版本一致性，避免环境冲突。  
3. **CLI 工具**：提供类似 Cargo 的命令行接口，支持添加/移除依赖、运行任务、管理全局环境等操作。  
4. **灵活安装方式**：可为项目或全局安装依赖，类似 pipx 或 condax。  
5. **集成 GitHub Actions**：支持自动缓存环境，简化 CI/CD 流程。  
6. **Rust 开发**：基于 Rattler 库构建，提升性能与稳定性。  

**使用方法**：  
- 安装：通过命令行安装（如 `cargo install pixi` 或系统特定命令）。  
- 初始化工作区：`pixi init` 创建项目，`pixi add` 添加依赖。  
- 运行任务：`pixi task add` 定义任务，`pixi run` 执行。  
- 全局安装：`pixi global install` 管理全局工具。  
- GitHub Actions 集成：通过 `setup-pixi` 动作自动安装依赖。