### [docker-slim docker-slim](https://github.com/docker-slim/docker-slim)  ![GitHub Repo stars](https://img.shields.io/github/stars/docker-slim/docker-slim?style=social)

Slim（原名 DockerSlim）是 CNCF 沙盒项目，旨在优化容器体验。其核心功能包括：

1. **镜像精简**：利用静态与动态分析理解应用需求，自动移除冗余文件，可将镜像体积缩小高达 30 倍。
2. **安全加固**：自动生成 Seccomp 和 AppArmor 安全配置文件，减少攻击面，无需手动编写 Linux 安全策略。
3. **容器分析与调试**：提供 xray、lint、build、debug 等命令，支持查看镜像内容、反编译 Dockerfile、调试运行中容器及漏洞扫描。
4. **广泛兼容**：支持 Node.js、Python、Java、Go 等多种语言应用及多种基础镜像，支持 CI/CD 集成（如 Jenkins、GitHub Actions）和容器化运行。

项目旨在让开发者在不改变现有工作流的情况下，构建更小、更安全的容器镜像。