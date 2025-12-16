
---
title: grequests
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/spyoungtech/grequests?style=social) ](https://github.com/spyoungtech/grequests)
### [spyoungtech grequests](https://github.com/spyoungtech/grequests)

**核心内容总结：**  
GRequests 是一个基于 Requests 和 Gevent 的异步 HTTP 请求库，支持并发发送请求以提高效率。  

**功能与使用方法：**  
1. **异步请求**：通过 `grequests.get` 等方法创建请求对象，使用 `map` 或 `imap` 并发发送多个请求。  
   - 示例：`rs = (grequests.get(u) for u in urls)`，`grequests.map(rs)`。  
2. **错误处理**：通过 `exception_handler` 参数捕获请求异常，自定义处理逻辑。  
3. **性能优化**：  
   - `imap` 返回生成器，适合处理大量请求（顺序不固定）。  
   - `imap_enumerated` 保留请求索引，可处理失败请求。  

**主要特性：**  
- 支持所有 Requests 的参数（如 `timeout`）。  
- 需先导入 `grequests` 再导入 `requests`，避免 Gevent 的 monkeypatching 冲突。  

**注意事项：**  
- 导入顺序需为 `import grequests` 在 `import requests` 之前。