
---
title: just
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/casey/just?style=social) ](https://github.com/casey/just)
### [casey just](https://github.com/casey/just)

**核心内容总结：**  
Just 是一个用于管理项目命令的工具，旨在简化开发流程中的常见操作（如构建、测试、部署等），避免 Make 的复杂性。其核心功能包括：  
1. **功能**：通过 `justfile` 定义命令，支持自定义脚本、依赖管理、环境变量配置等，所有命令默认视为“伪目标”（类似 Make 的 `.PHONY`），无需额外声明。  
2. **使用方法**：  
   - 创建 `justfile` 文件，定义命令（如 `test: cargo test`）。  
   - 使用 `just <命令名>` 执行，支持参数传递（如 `just build --release`）。  
   - 可通过 `just --list` 查看可用命令。  
3. **主要特性**：  
   - **跨平台**：基于 Rust 开发，兼容多操作系统。  
   - **简洁语法**：无需复杂配置，命令自动视为伪目标，避免 Make 的歧义问题。  
   - **可扩展**：支持自定义属性（如 `shell` 指定执行环境）、全局/项目级命令、远程执行等。  
   - **与 Make 的区别**：无需 `.PHONY` 声明，命令直接执行，不依赖文件状态判断是否跳过。  
4. **适用场景**：适合需要频繁执行多步骤命令的项目，尤其适用于团队协作中统一操作流程。