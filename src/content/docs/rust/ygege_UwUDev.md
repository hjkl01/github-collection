
---
title: ygege
---

### [UwUDev ygege](https://github.com/UwUDev/ygege)  ![GitHub Repo stars](https://img.shields.io/github/stars/UwUDev/ygege?style=social)

Ygégé 是一款基于 Rust 编写的高性能 YGG Torrent 索引器。主要功能包括自动解析当前域名、自动化绕过 Cloudflare 验证（无需手动处理）、近乎即时搜索、会话自动重连与缓存、绕过虚假 DNS 以及低内存占用（14.7MB）。支持按名称、种子数、日期等多种条件进行模块化搜索，并获取描述、大小等详细信息。项目无需浏览器驱动或外部依赖，通过 `wreq` 库模拟真实浏览器 TLS/HTTP/2 通信以规避指纹检测。支持 Docker 及源码安装，并可作为自定义索引器集成至 Prowlarr 和 Jackett。