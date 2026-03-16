### [Boris-code feaplat](https://github.com/Boris-code/feaplat)  ![GitHub Repo stars](https://img.shields.io/github/stars/Boris-code/feaplat?style=social)

feaplat 是一款基于 Docker Swarm 的分布式爬虫管理系统，核心功能如下：

1. **多框架支持**：兼容 feapder、scrapy 等任意 Python 脚本，支持 Playwright 和 Selenium 浏览器渲染（含无头/有头模式）。
2. **弹性架构**：Master 调度与 Worker 执行分离，Worker 节点随任务动态生成，任务完成后自动销毁，支持弹性伸缩与自动负载均衡。
3. **任务管理**：支持项目编辑、4 种定时启动方式、任务实例日志查看及自定义监控内容。
4. **集群与环境定制**：支持服务器集群管理、多实例分布式运行，允许自定义 Worker 镜像以适配特殊环境（如 Java、机器学习）。
5. **便捷部署**：提供 Docker 一键部署方案，支持私有项目拉取与集群节点扩展。