
---
title: llama-swap
---

### [mostlygeek llama-swap](https://github.com/mostlygeek/llama-swap)  ![GitHub Repo stars](https://img.shields.io/github/stars/mostlygeek/llama-swap?style=social)

llama-swap 是一款基于 Go 开发的轻量级代理工具，旨在实现本地生成式 AI 模型的热切换与统一管理。它兼容 OpenAI 和 Anthropic 协议，可对接 llama.cpp、vllm 等多种推理后端。

核心功能：
1. **动态模型管理**：根据请求自动加载、切换或卸载模型，支持多模型分组并行运行。
2. **广泛接口支持**：涵盖 OpenAI（文本、音频、图像）、Anthropic 及 llama-server 的多种标准 API 端点。
3. **极简部署**：零外部依赖，仅需二进制文件和配置文件，支持 Docker、Homebrew 及源码安装。
4. **内置 Web UI**：提供实时日志流、Token 指标监控、请求响应审查、模型沙盒测试及手动控制功能。
5. **灵活配置**：支持 API 密钥鉴权、模型自动超时卸载、启动钩子及请求过滤器。