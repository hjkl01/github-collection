
---
title: mise
---

### [jdx mise](https://github.com/jdx/mise)

**核心内容总结：**  
`mise` 是一个集成开发环境管理工具，结合了 `asdf`（多语言版本管理）、`direnv`（环境变量管理）和 `make`（任务自动化）的功能，用于统一管理开发工具、环境变量和项目任务。  

**主要功能：**  
- **开发工具管理**：支持 Node.js、Python、Go、Terraform 等数百种工具的多版本安装与切换。  
- **环境变量管理**：通过 `mise.toml` 配置文件定义项目级环境变量，或加载 `.env` 文件实现环境隔离。  
- **任务自动化**：在 `mise.toml` 中定义任务（如构建、测试），支持依赖关系和命令执行。  

**使用方法：**  
1. **安装**：通过 `curl https://mise.run | sh` 安装，随后根据 Shell 类型（Bash/Zsh/Fish/PowerShell）配置激活命令。  
2. **配置工具**：在 `mise.toml` 中指定工具版本（如 `[tools] terraform = "1"`）。  
3. **执行命令**：使用 `mise exec <tool@version> -- <command>` 运行特定版本工具，或通过 `mise use` 全局安装工具。  
4. **管理环境变量**：在 `mise.toml` 的 `[env]` 段定义变量，或使用 `mise set VAR=value` 动态设置。  
5. **运行任务**：在 `mise.toml` 的 `[tasks]` 段定义任务（如 `[tasks.build] run = "npm install"`），通过 `mise run build` 执行。  

**特性亮点：**  
- 支持跨平台（macOS/Windows/Linux）。  
- 工具安装路径可直接通过 `which <tool>` 查看真实路径，非符号链接。  
- 提供官方文档、演示视频及社区讨论（GitHub Discussions）。