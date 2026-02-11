
---
title: llama-swap
---

### [mostlygeek llama-swap](https://github.com/mostlygeek/llama-swap)  ![GitHub Repo stars](https://img.shields.io/github/stars/mostlygeek/llama-swap?style=social)

**项目名称**：llama-swap

**项目功能**：  
llama-swap 是一个用 Go 编写的高性能工具，允许用户在同一台机器上运行多个本地 LLM 模型，并在需要时动态切换模型，而无需重启应用程序。它支持所有 OpenAI API 兼容的服务器，如 llama.cpp、vllm、tabbyAPI 等，具备灵活的模型管理与自动切换能力。

**使用方法**：  
- 提供多种安装方式：Docker、Homebrew、WinGet、预编译二进制文件、源码编译。
- 配置文件简单，只需一个 YAML 文件即可定义模型及其启动命令。
- 可通过 Web UI 实时监控日志、管理模型。
- 支持 API 密钥限制访问，提供多个 API 端点用于模型管理与日志查看。

**主要特性**：
- **简单部署**：一个二进制文件，一个配置文件，无外部依赖。
- **模型热切换**：根据请求自动加载或切换模型。
- **支持多种模型服务器**：兼容 OpenAI、Anthropic API，支持 llama-server 等特定端点。
- **Web UI 界面**：提供实时日志监控、模型控制、请求历史查看。
- **高级功能**：支持模型分组、自动卸载、预加载、端口自动分配、请求过滤、环境变量设置等。
- **Docker 支持**：提供多种平台的容器镜像，支持非 root 运行。
- **反向代理配置建议**：提供 nginx 配置示例，确保流式请求正常工作。
- **CLI 日志监控**：支持通过命令行查看或流式读取模型与系统日志。

**适用场景**：  
适用于本地部署多个 LLM 模型的用户，需要灵活切换模型以满足不同任务需求，同时希望简化部署与管理流程。