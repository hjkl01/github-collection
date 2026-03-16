### [spyoungtech grequests](https://github.com/spyoungtech/grequests)  ![GitHub Repo stars](https://img.shields.io/github/stars/spyoungtech/grequests?style=social)

GRequests 是基于 Requests 库和 Gevent 的 Python 项目，用于实现异步 HTTP 请求。

主要功能包括：
1. 批量异步发送：使用 map 方法同时发送多个请求。
2. 接口兼容：支持 requests 库的所有 HTTP 动词及参数。
3. 异常处理：支持自定义异常处理器捕获超时或连接错误。
4. 性能优化：提供 imap 和 imap_enumerated 方法支持流式处理及并发池调整。
5. 导入规范：需先导入 grequests 以避免 gevent 猴子补丁冲突。