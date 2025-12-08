
---
title: kulala.nvim
---

### [mistweaverco kulala.nvim](https://github.com/mistweaverco/kulala.nvim)

**核心内容总结：**

**项目功能**  
kulala.nvim 是一款为 Neovim 设计的 REST 客户端插件，支持在编辑器内发起 HTTP 请求，兼容 IntelliJ HTTP Client 规范。支持协议包括 HTTP、gRPC、GraphQL、WebSocket 和流媒体，可导入/导出 Postman、OpenAPI 等格式，提供脚本编写（JS/Lua）、认证（OAuth2、AWS 等）、响应格式化、自动化测试等功能。

**使用方法**  
通过 [lazy.nvim](https://github.com/folke/lazy.nvim) 安装，配置后使用 `<leader>Rs`（发送单个请求）、`<leader>Ra`（发送所有请求）、`<leader>Rb`（打开草稿区）等快捷键操作。需 Neovim 0.10.0+ 和 cURL 环境。

**主要特性**  
- 支持 HTTP 文件规范及动态变量（环境、文档、请求等）  
- 内置 LSP 自动补全与格式化  
- 脚本功能：预请求、后请求、条件判断、外部脚本  
- 响应过滤、断言测试与报告生成  
- 支持从文件导入请求，保存响应数据  
- 与 Kulala Language Server 和 Formatter 工具联动，提供完整 REST 客户端体验