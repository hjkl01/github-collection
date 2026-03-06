
---
title: pydoll
---

### [autoscrape-labs pydoll](https://github.com/autoscrape-labs/pydoll)  ![GitHub Repo stars](https://img.shields.io/github/stars/autoscrape-labs/pydoll?style=social)

Pydoll 是一款基于 Python 的异步浏览器自动化工具，通过 WebSocket 直接连接 Chrome DevTools Protocol (CDP) 控制 Chromium 内核浏览器（如 Chrome、Edge）。

核心功能总结：
1. **反检测与指纹控制**：无需 WebDriver 二进制文件，隐藏 `navigator.webdriver` 标识，支持人类化鼠标移动、物理震颤模拟及浏览器偏好定制。
2. **网络控制**：支持请求拦截、流量监控、HAR 录制与回放，以及继承浏览器会话（Cookies、Headers）的认证 HTTP 请求。
3. **高级 DOM 操作**：完整支持 Shadow DOM（含闭合模式）、iframe 及跨域元素查询与交互。
4. **混合自动化**：结合 UI 流程（如处理登录/验证码）与高性能 API 调用，无缝切换。
5. **其他特性**：页面资源打包、多标签/上下文并发管理、重试装饰器、屏幕截图及 PDF 生成。

项目异步原生且全类型检查，安装仅需 `pip install pydoll-python`，无外部依赖。