
---
title: chrome-devtools-mcp
---

### [ChromeDevTools chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)  ![GitHub Repo stars](https://img.shields.io/github/stars/ChromeDevTools/chrome-devtools-mcp?style=social)

`chrome-devtools-mcp` 是一个 Model-Context-Protocol (MCP) 服务器，使 AI 编程助手（如 Gemini、Claude、Cursor 等）能够控制并检查实时 Chrome 浏览器。

核心功能包括：
1. **性能分析**：利用 Chrome DevTools 记录跟踪并提取性能洞察。
2. **高级调试**：支持分析网络请求、截图、检查浏览器控制台消息（含源映射堆栈）。
3. **自动化操作**：基于 Puppeteer 实现页面导航、输入、点击等浏览器操作，并自动等待结果。
4. **多功能工具**：涵盖输入自动化、页面管理、模拟、性能分析、网络监控及脚本调试（如 Lighthouse 审计）。
5. **灵活连接**：支持自动启动 Chrome 实例，或连接已运行的实例（通过调试端口/WebSocket），支持无头模式及自定义配置。
6. **环境要求**：需 Node.js v20+ 和最新版 Chrome，默认收集使用统计（可禁用）。