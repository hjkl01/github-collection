
---
title: AIClient-2-API
---

### [justlovemaki AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API)  ![GitHub Repo stars](https://img.shields.io/github/stars/justlovemaki/AIClient-2-API?style=social)

AIClient-2-API 是一个 API 代理服务，能够将 Gemini CLI、Antigravity、Qwen Code、Kiro 等客户端独占的大模型接口转换为标准的 OpenAI 兼容接口。支持 Gemini、Claude、Grok、Qwen 等多模型统一接入，通过智能协议转换使现有客户端工具（如 Cherry-Studio、NextChat）无需修改即可调用高级模型。核心功能包括突破官方限制（如绕过 Cloudflare 封锁）、内置账户池管理（多账户轮询、自动故障转移、健康检查）、Web UI 可视化配置、Docker 部署及全链路日志审计。项目支持 TLS 指纹旁路、私有数据集构建及本地化数据安全，确保服务的高可用性（99.9%）。