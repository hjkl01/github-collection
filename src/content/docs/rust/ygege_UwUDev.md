
---
title: ygege
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/UwUDev/ygege?style=social) ](https://github.com/UwUDev/ygege)
### [UwUDev ygege](https://github.com/UwUDev/ygege)

**项目核心内容总结**：

Ygégé 是一个用 Rust 编写的高性能 YGG Torrent 索引器，支持自动解析 YGG 域名、绕过 Cloudflare 防护、快速搜索与会话恢复等功能。其主要特性包括：低内存占用（Linux 发布版仅 14.7MB）、无需浏览器驱动、支持按名称、种子数等条件搜索、获取详细 torrent 元数据、无外部依赖。  

**使用方法**：  
- 提供 Docker 镜像，可通过 [Docker 指南](docs/docker-guide.md) 部署；  
- 支持手动编译，参考 [源码安装指南](docs/source-guide.md)；  
- 集成至 Prowlarr 或 Jackett：将 `ygege.yml` 配置文件复制到对应程序的 AppData 目录，重启后即可在索引器设置中使用。  

**其他说明**：  
- 通过模拟浏览器行为（基于 wreq 库）实现 Cloudflare 绕过；  
- 提供 IMDB/TMDB 元数据支持，需按 [指南](docs/tmdb-imdb.md) 配置；  
- 性能测试显示搜索响应时间约 176ms/次（100 次测试平均）。