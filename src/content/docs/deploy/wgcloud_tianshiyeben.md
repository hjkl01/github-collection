
---
title: wgcloud
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/tianshiyeben/wgcloud?style=social) ](https://github.com/tianshiyeben/wgcloud)
### [tianshiyeben wgcloud](https://github.com/tianshiyeben/wgcloud)

**WGCLOUD运维监控系统核心内容总结：**

**项目功能**  
WGCLOUD是一款轻量级分布式监控系统，支持实时监控服务器硬件（CPU、内存、磁盘等）、进程、端口、日志、Docker容器、数据库等资源，提供网络拓扑生成、大屏可视化、Web SSH（堡垒机）、告警推送（邮件/钉钉/微信等）、批量指令执行等功能。支持监测Linux、Windows、macOS、Unix等主流平台，兼容ARM、Android、RISC-V等架构。

**使用方法**  
1. 使用IDEA或Eclipse导入`wgcloud-server`和`wgcloud-agent`模块，需安装JDK 1.8或11。  
2. 在MySQL数据库中创建`wgcloud`数据库并导入`wgcloud.sql`脚本。  
3. 通过`bin`目录下的脚本启动服务端和代理端（支持Linux/Windows）。  

**主要特性**  
- 采用OSHI组件采集主机指标，替代旧版Sigar方式。  
- 服务端与代理端协同工作，支持数千台主机并发监控。  
- 开源版功能完整，商业版提供更高性能、安全性及稳定性（需官网下载）。  
- 支持自定义监控项、硬件健康状态检测、文件防篡改、网络设备监控等。  
- 提供在线文档、演示系统及多平台部署方案。  

**其他说明**  
开源版代码可直接在GitHub获取，生产环境建议使用商业版本。