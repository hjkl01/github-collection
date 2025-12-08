
---
title: ngxtop
---

### [lebinh ngxtop](https://github.com/lebinh/ngxtop)

**项目功能**  
`ngxtop` 是一个用于实时监控 Nginx 服务器（及其他服务器）的工具，通过解析访问日志输出类似 `top` 的指标，帮助用户实时了解服务器运行状态（如请求路径、响应状态码、流量来源等）。支持分析 Nginx 和 Apache 日志，可自定义日志格式、分组规则、过滤条件等。

**使用方法**  
- 安装：`pip install ngxtop`  
- 基础命令：`ngxtop`（默认解析 Nginx 访问日志并展示请求路径、状态码等统计信息）  
- 高级用法：  
  - 按字段排序：`ngxtop top remote_addr`（查看访问 IP 排行）  
  - 过滤数据：`ngxtop -i 'status >= 400' print request status http_referer`（筛选 4xx/5xx 请求并显示来源）  
  - 解析 Apache 日志：`ngxtop -f common`（指定日志格式为 Apache 的 `common` 格式）  

**主要特性**  
1. 自动识别日志文件路径和格式，支持自定义配置。  
2. 实时监控（默认仅关注新增日志，可选处理历史日志）。  
3. 灵活的分组、排序、过滤功能（如按请求路径、IP、状态码等）。  
4. 支持输出统计指标（如请求数、平均字节数、响应码分布等）。  
5. 兼容 Python 2 和 3，可通过管道处理远程日志流（如 `tail -f | ngxtop`）。