
---
title: gofound
---

### [sea-team gofound](https://github.com/sea-team/gofound)

**GoFound** 是一个用 Golang 实现的全文检索引擎，支持持久化存储和单机亿级数据毫秒级检索。通过 HTTP 接口调用，提供倒排索引、正排索引、文件分片、中文分词（基于 golang-jieba）等技术，内存占用低，无需依赖外部组件。  

**主要特性**：  
- 支持持久化存储，数据可长期保存；  
- 单机处理亿级数据，查询速度达毫秒级；  
- 内置中文分词及词库，无需额外配置；  
- 基于磁盘+内存缓存，内存占用远低于 Elasticsearch；  
- 提供可视化管理界面及 API 文档；  
- 支持多语言 SDK（Java/Python/Node.js 等），或直接通过 HTTP 接口调用。  

**使用方法**：  
- 下载二进制文件或源码编译后运行（`./gofound --addr=:8080 --data=./data`）；  
- 支持 Docker 部署（需挂载数据目录）；  
- 配置参数参考文档，支持灵活调整。
