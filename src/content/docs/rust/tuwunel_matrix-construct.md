
---
title: tuwunel
---

### [matrix-construct tuwunel](https://github.com/matrix-construct/tuwunel)  ![GitHub Repo stars](https://img.shields.io/github/stars/matrix-construct/tuwunel?style=social)

Tuwunel 是一个用 Rust 编写的高性能 Matrix 家居服务器（homeserver），作为 Synapse 的替代方案，支持所有主流 Matrix 客户端、桥接器和机器人。该项目完全实现了 Matrix 规范，适用于大多数场景，具有可扩展性、低成本、企业级、社区驱动等优点。

### 核心内容总结：

- **项目功能**：
  - 提供完整的 Matrix 协议支持。
  - 作为 Matrix 家居服务器，支持用户注册、消息通信、房间管理等。
  - 支持多种部署方式，包括 Docker、静态二进制文件、Deb/RPM 包、Arch AUR、Nix 包等。
  - 提供 TLS 证书支持，推荐使用 Caddy 作为反向代理。
  - 提供官方文档和部署指南。

- **使用方法**：
  - 通过 `tuwunel-example.toml` 配置文件设置服务器名称和数据库路径。
  - 启动服务器后，通过客户端连接并注册用户，第一个注册用户为管理员。
  - 可通过 Caddy 配置反向代理，实现 HTTPS 自动管理。
  - 支持从 conduwuit 无缝迁移，只需替换可执行文件。

- **主要特性**：
  - 用 Rust 实现，性能高、内存安全。
  - 支持多种部署方式，适合企业级使用。
  - 提供文档、演示服务器和社区支持。
  - 强调“同理心”主题，倡导在通信中体现关怀与责任。
  - 支持从 conduwuit 迁移，但不支持从 Synapse 或其他 Conduit 分支迁移。

- **迁移支持**：
  - 从 conduwuit 迁移：支持，只需替换可执行文件。
  - 从 Synapse 迁移：尚未支持，但计划中。
  - 从 Conduit 或其分支迁移：不支持，可能造成数据库损坏。

- **升级与降级**：
  - 降级通常安全，但可能受版本限制。
  - 推荐使用 `:latest` 或 `:preview` Docker 标签进行自动更新。

- **支持与帮助**：
  - 提供 GitHub Issues、Matrix 社区聊天室和私信支持。
  - 有非官方社区聊天室，但项目方不直接管理。