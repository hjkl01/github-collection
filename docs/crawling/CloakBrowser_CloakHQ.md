### [CloakBrowser](https://github.com/CloakHQ/CloakBrowser) ![GitHub Repo stars](https://img.shields.io/github/stars/CloakHQ/CloakBrowser?style=social)

CloakBrowser 是一个基于 Chromium 源码级补丁的“隐身浏览器”，可直接替代 Python/JavaScript 中的 Playwright 或 Puppeteer（基本只需改导入），用于降低自动化被识别和拦截的概率。其核心能力包括：

- 通过大量 C++ 源码级指纹补丁（如 canvas、WebGL、音频、字体、GPU、WebRTC、自动化信号、CDP 行为等），而非 JS 注入或配置伪装，实现更真实的浏览器特征。  
- 支持 `humanize` 人类行为模拟（鼠标轨迹、键盘节奏、滚动模式等），提升行为层反检测效果。  
- 支持 HTTP/SOCKS5 代理、基于代理 IP 自动匹配时区与语言、WebRTC IP 伪装、持久化用户配置（cookie/localStorage）等。  
- 提供 Python 与 Node.js 完整 API（同步/异步、普通启动、上下文启动、持久化上下文），并支持 CLI、Docker、CDP 远程连接。  
- 二进制自动下载、缓存与自动更新，开箱即用（`pip install` / `npm install`）。  
- 提供自托管 Browser Profile Manager（可创建多指纹配置、代理与持久会话）。  
- 项目开源免费（包装器 MIT），定位为生产可用的反检测自动化浏览器基础设施。