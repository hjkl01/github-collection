
---
title: goalert
---

### [target goalert](https://github.com/target/goalert)

GoAlert 是一个提供值班调度、自动升级和多渠道通知（如短信、语音）的系统，用于在合适的时间通过正确方式联系相关人员。  

**使用方法**  
- 可通过 GitHub Releases 下载二进制文件，或使用 Docker Hub 镜像（如 `docker run -it --rm -p 8081:8081 goalert/demo`）快速启动，访问地址为 `localhost:8081`，默认登录凭据为 `admin`/`admin123`。  
- 开发环境可通过 `make start` 启动，服务运行在 `localhost:3030`，支持本地代码修改实时生效。  

**主要特性**  
- 支持自动化升级规则和多类型通知；  
- 提供演示环境及测试用户（`user`/`user1234`）；  
- 开发者可跳过初始化数据（通过 `SKIP_SEED=1` 环境变量）；  
- 提供 API 获取会话令牌（如通过 `curl` 命令）。  

**许可证**  
采用 Apache License 2.0 开源协议。