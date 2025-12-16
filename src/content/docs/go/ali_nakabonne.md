
---
title: ali
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/nakabonne/ali?style=social) ](https://github.com/nakabonne/ali)
### [nakabonne ali](https://github.com/nakabonne/ali)

**项目核心内容总结：**  
`ali` 是一个受 Vegeta 和 jplot 启发的负载测试工具，支持实时分析和终端内嵌图表展示。  

**功能特点：**  
- 提供终端实时图表（如延迟、百分位数等），支持鼠标交互操作；  
- 可自定义请求参数（如方法、速率、持续时间、请求体等）；  
- 支持多种安装方式（Homebrew、APT、Go 等）；  
- 可通过命令行直接发起测试，默认参数为速率 50 RPS、持续时间 10 秒。  

**使用方法：**  
1. 安装后通过 `ali <目标URL>` 启动测试；  
2. 按回车开始攻击，使用 `-d` 设置持续时间、`-r` 设置速率等参数；  
3. 实时图表可通过 `l`/`h` 切换显示内容，支持区域缩放。  

**主要特性：**  
- 实时绘图与进度可视化；  
- 支持 HTTP/2、TLS 配置及自定义 DNS 解析；  
- 基于 termdash 实现终端图形渲染，兼容鼠标操作。