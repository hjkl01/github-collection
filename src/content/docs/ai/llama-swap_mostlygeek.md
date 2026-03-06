
---
title: llama-swap
---

### [mostlygeek llama-swap](https://github.com/mostlygeek/llama-swap)  ![GitHub Repo stars](https://img.shields.io/github/stars/mostlygeek/llama-swap?style=social)

llama-swap 是一个基于 Go 开发的轻量级代理工具，用于在本地运行多个生成式 AI 模型并支持按需热切换。它兼容 OpenAI 和 Anthropic 标准 API 接口，可对接 llama.cpp、vllm、tabbyAPI 等多种推理服务器。项目无需外部依赖，仅通过一个二进制文件和一个配置文件即可部署。核心功能包括：动态模型管理（自动加载/卸载、超时清除、多模型分组）、完整的 API 端点支持（涵盖聊天、图像、音频、嵌入等）、内置实时 Web UI 管理界面（支持日志监控、请求审查及模型控制）、API 密钥鉴权以及完善的 Docker 部署支持。该工具通过自动交换上游服务器来处理不同模型的请求，极大简化了本地 AI 工作流的配置与管理。