
---
title: readyset
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/readysettech/readyset?style=social) ](https://github.com/readysettech/readyset)
### [readysettech readyset](https://github.com/readysettech/readyset)

**核心内容总结：**  
Readyset 是一个透明的数据库缓存工具，兼容 PostgreSQL 和 MySQL，无需修改应用代码或手动处理缓存失效即可实现高性能读取。它通过数据库复制流自动同步缓存数据，提供类似内存键值存储的性能和可扩展性。  

**主要功能与特性：**  
- 自动同步缓存与数据库，无需人工干预；  
- 协议兼容，可无缝集成现有 ORM 或数据库客户端；  
- 支持复杂 SQL 查询的快速响应；  
- 提供云服务（Readyset Cloud）实现数据库自动扩展。  

**使用方法：**  
通过命令行脚本（`bash -c "$(curl -sSL https://launch.readyset.io)"`）、Docker 镜像或 Linux 二进制文件安装；也可通过 Readyset Cloud 使用托管服务。  

**其他信息：**  
- 开源许可证为 BSL 1.1（4 年后转为 Apache 2.0）；  
- 提供文档、博客、社区支持（Slack、GitHub）及贡献指南。