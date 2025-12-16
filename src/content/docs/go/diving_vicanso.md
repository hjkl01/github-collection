
---
title: diving
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/vicanso/diving?style=social) ](https://github.com/vicanso/diving)
### [vicanso diving](https://github.com/vicanso/diving)

**项目核心内容总结：**  
该项目用于通过网站分析 Docker 镜像，基于 [dive](https://github.com/wagoodman/dive) 工具获取分析信息。首次使用时需先拉取镜像，可能稍慢。  

**使用方法：**  
通过 Docker 命令运行容器，挂载 `/var/run/docker.sock` 卷并映射 7001 端口。  

**主要特性：**  
- 使用 Rust 开发，性能更快、更简洁；  
- 已存档，推荐使用 [diving-rs](https://github.com/vicanso/diving-rs) 替代。