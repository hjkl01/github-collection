
---
title: prek
---

### [j178 prek](https://github.com/j178/prek)  ![GitHub Repo stars](https://img.shields.io/github/stars/j178/prek?style=social)

**项目核心内容总结：**

prek 是一个用 Rust 编写的 pre-commit 替代工具，旨在提供更快、无依赖且功能增强的代码钩子管理方案。其核心功能包括：  
- **兼容性**：完全支持原有 pre-commit 的配置和钩子，可无缝替换。  
- **性能优化**：比 pre-commit 快数倍，磁盘占用减少一半，支持并行克隆仓库、并行安装依赖和按优先级并行运行钩子。  
- **无依赖设计**：无需安装 Python 或其他运行时，单个二进制文件即可运行。  
- **增强功能**：内置 Rust 实现的常见钩子（如格式化、类型检查），支持多仓库（monorepo）模式，集成 uv 管理 Python 虚拟环境，提供 `prek run --directory`、`--last-commit` 等便捷命令。  

**使用方法**：  
- **安装**：支持通过脚本下载、PyPI、Homebrew、cargo 等方式安装，也可通过 GitHub Actions 集成。  
- **使用**：通过 `.pre-commit-config.yaml` 配置钩子，使用 `prek run` 执行检查，`prek list` 查看钩子信息，`prek auto-update` 管理更新。  

**主要特性**：  
- 无依赖、单文件部署；  
- 支持多仓库（monorepo）独立配置；  
- 内置 Rust 钩子提升性能；  
- 集成 uv 实现高效 Python 依赖管理；  
- 提供更便捷的命令行操作（如指定目录、提交记录运行钩子）。  

**应用案例**：已被 Apache Airflow、FastAPI、Django 等知名项目采用。