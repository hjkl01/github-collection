
---
title: proxypool
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/henson/proxypool?style=social) ](https://github.com/henson/proxypool)
### [henson proxypool](https://github.com/henson/proxypool)

该项目是一个用Go语言实现的IP代理池，用于采集免费代理资源并验证其有效性，为爬虫提供可用的代理IP。  

**核心功能**：  
1. **代理采集**：支持从9个免费代理网站（如66ip、ip181、Proxylist+等）抓取IP，并可扩展自定义采集接口。  
2. **代理验证**：通过定时任务检测代理可用性，过滤掉无效或速度过慢（≥1秒）的代理。  
3. **数据库支持**：使用xorm框架，兼容MySQL、PostgreSQL、SQLite3等数据库，支持数据自动更新与去重。  
4. **API接口**：提供HTTP接口（如`/v2/ip`、`/v2/https`）返回随机可用代理，支持爬虫直接调用。  

**使用方法**：  
- 安装依赖（如PhantomJS）后，通过`go get`下载项目，修改配置文件`app.ini`（设置数据库、日志等参数），执行`go build`并启动服务。  
- 通过HTTP接口获取代理，支持自定义扩展采集函数并修改`main.go`中的调用逻辑。  

**主要特性**：  
- 支持多平台（含MAC）及多种数据库类型；  
- 容错机制确保单个采集错误不影响整体运行；  
- 日志系统支持文件输出、自动轮转及分级记录；  
- 提供代理速度检测与自动过滤功能。