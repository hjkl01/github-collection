
---
title: scan4all
---

### [hktalent scan4all](https://github.com/hktalent/scan4all)

**项目核心内容总结：**

**功能：**  
scan4all 是一款集成漏洞扫描、弱密码爆破、端口扫描及 HTTP 漏洞检测的网络安全工具，支持多协议（如 FTP、SSH、SMB 等）弱密码检测，集成 Nuclei 模板实现漏洞验证，支持 HTTP 走私、缓存投毒检测，并可与 Elasticsearch 联动存储扫描结果。

**使用方法：**  
1. 安装 Elasticsearch 并初始化索引；  
2. 下载 scan4all 工具（提供预编译版本或通过 Go 安装）；  
3. 通过命令行参数指定扫描目标（如 `-l xx.txt`）、协议（如 `-tp http`）及自定义配置（如 `UrlPrecise=true`）；  
4. 扫描结果默认存储至 Elasticsearch，亦可传统输出。

**主要特性：**  
- 支持 11 种协议弱密码爆破，集成 3744+ Nuclei 漏洞检测模板；  
- 内置 HTTP 走私、缓存投毒检测模块；  
- 支持 Elasticsearch 数据存储与检索；  
- 可自定义指纹匹配规则、SSL 分析深度及子域名爆破字典；  
- 提供精准 URL 扫描模式与多线程扫描优化。