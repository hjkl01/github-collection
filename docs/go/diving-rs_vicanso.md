### [vicanso diving-rs](https://github.com/vicanso/diving-rs)  ![GitHub Repo stars](https://img.shields.io/github/stars/vicanso/diving-rs?style=social)

diving-rs 是一款基于 Rust 开发的快速简单的 Docker 镜像分层探索工具，无需依赖 Docker 客户端，兼容 Linux、Windows 和 MacOS 平台。支持终端（默认）和 Web 两种模式，可从 Docker 注册表、本地 Docker 客户端或 Tar 文件获取镜像进行分析。终端模式支持查看当前层文件内容、过滤修改/删除文件及大于 1MB 的文件，并支持自定义层缓存路径和过期时间。Web 模式支持通过 Docker 容器部署，通过浏览器访问界面进行交互分析。