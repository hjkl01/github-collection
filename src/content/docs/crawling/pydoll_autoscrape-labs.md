
---
title: pydoll
---

### [autoscrape-labs pydoll](https://github.com/autoscrape-labs/pydoll)  ![GitHub Repo stars](https://img.shields.io/github/stars/autoscrape-labs/pydoll?style=social)

Pydoll 是一个基于 Python 的异步原生浏览器自动化工具，专为 Chromium 内核浏览器（如 Chrome、Edge）设计。它通过 WebSocket 直接连接 Chrome DevTools Protocol (CDP)，无需 WebDriver 或外部依赖。

主要功能包括：
1. **高隐蔽性**：模拟人类鼠标操作，精细控制浏览器指纹，规避反爬虫检测。
2. **混合自动化**：结合 UI 操作与 API 请求，可复用浏览器会话（Cookie、Header）进行网络调用。
3. **网络控制**：支持请求拦截、流量监控、广告屏蔽、HAR 录制与重放。
4. **DOM 交互**：全面支持 Shadow DOM（包括封闭模式）和跨域 iframe 的元素查询与交互。
5. **技术特性**：基于 asyncio 构建，全代码库类型检查，支持并发、多标签页/上下文管理及远程浏览器连接。