
---
title: grok2api
---

### [chenyme grok2api](https://github.com/chenyme/grok2api)  ![GitHub Repo stars](https://img.shields.io/github/stars/chenyme/grok2api?style=social)

Grok2API 是一个基于 FastAPI 重构的 Grok 服务代理项目，核心功能总结如下：

1. **多模态与对话支持**：全面适配 Grok 最新 Web 调用格式，支持文本对话（含深度思考）、图像生成/编辑、视频生成/超分（文生视频/图生视频）及工具调用。
2. **接口兼容**：兼容 OpenAI 标准接口格式（如 `/v1/chat/completions`, `/v1/responses`, `/v1/images/*`），支持流式与非流式输出。
3. **资源与负载均衡**：内置号池并发与自动负载均衡机制，提供 Web 管理面板用于 Token 管理、状态筛选、批量操作、NSFW 模式一键开启及配置缓存管理。
4. **部署与存储**：支持本地、Docker Compose、Vercel、Render 等多种部署方式，支持本地文件、Redis、MySQL、PostgreSQL 等多种存储后端配置。