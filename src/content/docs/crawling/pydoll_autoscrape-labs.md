
---
title: pydoll
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/autoscrape-labs/pydoll?style=social) ](https://github.com/autoscrape-labs/pydoll)
### [autoscrape-labs pydoll](https://github.com/autoscrape-labs/pydoll)

**核心内容总结：**  
Pydoll 是一个专注于规避反爬虫检测的网页自动化框架，采用异步架构和类型化设计，支持高性能数据抓取与多任务并发。其核心功能包括：  
1. **混合自动化**：结合浏览器操作与 API 调用，支持多标签页、浏览器上下文隔离及远程连接，提升并发效率。  
2. **网络控制**：提供代理设置、SOCKS5 协议支持及 DNS 泄漏规避，强化网络层匿名性。  
3. **浏览器指纹规避**：通过精细调整 Chrome 内部设置（如通知权限、语言、字体等），降低被识别风险。  
4. **可靠性增强**：内置 `@retry` 装饰器支持自定义重试逻辑，配合类型检查确保代码稳定性。  
5. **使用方法**：通过 `pip` 安装后，使用异步代码启动浏览器，执行页面导航、元素定位及交互操作，支持多任务并行处理。  
6. **知识体系**：文档详细解析反爬技术原理（如网络指纹、行为分析）及规避策略，帮助用户深入理解自动化与反爬对抗逻辑。