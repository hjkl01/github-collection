
---
title: starlette
---

### [Kludex starlette](https://github.com/Kludex/starlette)

**核心内容总结：**

Starlette 是一个轻量级的 ASGI 框架/工具包，用于构建 Python 异步 Web 服务。主要功能包括：  
- 支持 HTTP 和 WebSocket 协议；  
- 提供异步背景任务、启动/关闭事件、测试客户端（基于 httpx）；  
- 内置 CORS、GZip、静态文件处理、流式响应等功能；  
- 支持会话、Cookie 管理，代码 100% 类型注解，测试覆盖率 100%。  

**使用方法：**  
1. 安装依赖：`pip install starlette` 和 ASGI 服务器（如 uvicorn）；  
2. 编写应用代码，定义路由和异步处理函数；  
3. 使用 `uvicorn main:app` 启动服务。  

**主要特性：**  
- 轻量、低复杂度，兼容 asyncio 和 trio；  
- 模块化设计，可独立使用组件；  
- 依赖少，支持通过 `starlette[full]` 安装所有可选功能（如 Jinja2 模板、表单解析等）；  
- 高性能，通过独立基准测试验证。