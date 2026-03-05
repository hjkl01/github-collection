
---
title: grequests
---

### [spyoungtech grequests](https://github.com/spyoungtech/grequests)  ![GitHub Repo stars](https://img.shields.io/github/stars/spyoungtech/grequests?style=social)

GRequests 是一个基于 Requests 和 Gevent 的库，支持通过 map 或 imap 等方法批量并发发送异步 HTTP 请求。它保留 Requests 原有接口并允许自定义异常处理及调整并发池大小。使用时需确保优先导入 grequests 以避免 Gevent 猴子补丁导致的兼容性问题。