### [caddy-docker-proxy](https://github.com/lucaslorentz/caddy-docker-proxy) ![GitHub Repo stars](https://img.shields.io/github/stars/lucaslorentz/caddy-docker-proxy?style=social)

Caddy-Docker-Proxy 是一个让 Caddy 通过 Docker 标签自动为容器或 Swarm 服务生成反向代理配置的插件。

它会扫描 Docker 的容器、服务、配置和元数据，识别以 `caddy` 为前缀的标签，并将这些标签自动转换为 Caddyfile 配置，包括站点、全局选项、片段、匹配器、指令嵌套和路由规则等。配置变化时会自动重新生成内存中的 Caddyfile，并触发 Caddy 无停机平滑重载。

项目核心功能包括：
- 通过 Docker 标签自动暴露网站和服务，无需手写 Caddyfile；
- 自动将请求反向代理到容器 IP、容器端口、服务 DNS 名称或 Swarm task IP；
- 支持自动 HTTPS，可自动申请和续期证书；
- 支持 Go 模板语法，可动态引用容器/服务信息；
- 提供 `upstreams` 模板函数，自动生成可用上游地址；
- 支持路径转发、重写、重定向、WebSocket、多域名代理等常见场景；
- 支持 Docker Swarm 服务级标签和普通容器级标签两种代理方式；
- 支持三种运行模式：独立模式、控制器模式、服务器模式，适合单机和分布式集群；
- 支持通过 Docker configs 或基础 Caddyfile 扩展原始配置；
- 支持通过环境变量或 CLI 配置 Docker 连接、入口网络、标签前缀、轮询间隔等参数；
- 自动保存生成后的 Caddyfile，方便排查配置问题。

此外，项目提供多种 Docker 镜像形式，支持 Alpine、CI、ARM、Windows 和自定义构建，并强调在生产环境中应将 `/data` 挂载到持久化存储以保留证书数据。