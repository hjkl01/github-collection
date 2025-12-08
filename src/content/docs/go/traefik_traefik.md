
---
title: traefik
---

### [traefik traefik](https://github.com/traefik/traefik)

**核心内容总结：**

Traefik 是一个现代的 HTTP 反向代理和负载均衡器，旨在简化微服务的部署。它能自动与 Docker、Kubernetes、Consul 等基础设施集成，动态生成路由规则，用户只需配置一次即可自动适配服务变化。

**主要功能：**
- 自动动态更新配置（无需重启）
- 支持多种负载均衡算法和 HTTPS（含通配符证书）
- 提供 Web UI、访问日志、监控指标（Prometheus/Datadog 等）
- 支持 WebSocket、HTTP/2、gRPC
- 提供 REST API 和单文件二进制（含官方 Docker 镜像）

**使用方法：**
1. 通过 Docker 运行（需配置 `traefik.toml` 文件）
2. 下载二进制文件并运行
3. 克隆源码自行编译

**支持的后端：** Docker/Swarm、Kubernetes、ECS、文件配置等。

**注意事项：** 升级新版本需参考官方迁移文档。