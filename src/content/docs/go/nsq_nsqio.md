
---
title: nsq
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/nsqio/nsq?style=social) ](https://github.com/nsqio/nsq)
### [nsqio nsq](https://github.com/nsqio/nsq)

NSQ 是一个实时分布式消息平台，支持大规模消息处理（每天数十亿条），采用分布式和去中心化架构，无单点故障，确保高可用性与可靠消息传递。其核心特性包括：  
1. **功能**：支持多种数据格式（JSON、MsgPack、Protocol Buffers 等），提供 Go 和 Python 官方客户端库及多种第三方库；  
2. **部署**：所有参数通过命令行配置，二进制文件无运行时依赖，提供 Linux、Darwin、FreeBSD、Windows 的二进制安装包及 Docker 镜像；  
3. **可靠性**：保证消息传递可靠性，支持故障转移和高可用性；  
4. **应用**：被 Bitly、Stripe、Docker 等公司用于生产环境。