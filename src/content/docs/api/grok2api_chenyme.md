
---
title: grok2api
---

### [chenyme grok2api](https://github.com/chenyme/grok2api)  ![GitHub Repo stars](https://img.shields.io/github/stars/chenyme/grok2api?style=social)

### **项目核心内容总结**

#### **项目功能**
Grok2API 是一个基于 FastAPI 构建的 Grok2 API 适配工具，支持多种功能，包括：
- **对话聊天**：支持流式/非流式对话。
- **图像生成/编辑**：支持图像生成和图像编辑功能。
- **视频生成**：支持视频生成和超分辨率处理。
- **深度思考**：支持思维链（thinking）模式。
- **并发与负载均衡**：支持 Token 池并发和自动负载均衡。

#### **使用方法**
- **本地开发**：使用 `uv sync` 安装依赖，运行 `uv run main.py` 启动。
- **Docker 部署**：使用 `docker compose up -d` 部署。
- **云平台部署**：
  - **Vercel**：通过部署按钮部署，并设置相关环境变量。
  - **Render**：通过部署按钮部署，注意免费实例会休眠。

#### **管理面板**
- 访问地址：`http://<host>:8000/admin`，默认密码 `grok2api`。
- **功能**：
  - Token 管理（添加/删除/刷新/导出）。
  - NSFW 模式一键开启。
  - 配置管理、缓存管理等。

#### **主要特性**
- **多模型支持**：支持 Grok 系列多个模型（如 `grok-3`, `grok-4`, `grok-imagine-1.0` 等）。
- **接口丰富**：
  - `/v1/chat/completions`：通用接口，支持对话、图像、视频生成。
  - `/v1/images/generations`：图像生成接口。
  - `/v1/images/edits`：图像编辑接口。
- **配置灵活**：
  - 通过 `.env` 文件和 `config.toml` 配置。
  - 支持多种存储类型（`local`, `redis`, `mysql`, `pgsql`）。
- **高可用性**：
  - 支持 Token 自动刷新、失败重试、NSFW 开启等。
  - 支持并发控制、缓存清理等性能优化。

#### **注意事项**
- 项目已停止接受 PR 和暂停功能更新。
- 仅限于学习与研究用途，不得用于非法用途。