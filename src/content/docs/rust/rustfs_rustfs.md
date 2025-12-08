
---
title: rustfs
---

### [rustfs rustfs](https://github.com/rustfs/rustfs)

**项目核心内容总结：**

RustFS 是一个基于 Rust 语言开发的高性能分布式对象存储系统，支持 S3 兼容协议，适用于数据湖、AI 和大数据场景。其主要特性包括：  
- **高性能**：利用 Rust 的内存安全和并发优势，提供高效资源利用率；  
- **分布式架构**：支持横向扩展与故障容错；  
- **全功能 S3 兼容**：可无缝对接现有 S3 工具和应用；  
- **开源许可**：采用 Apache 2.0 协议，无 AGPL 限制，适合商业和社区开发；  
- **数据主权**：无数据 telemetry，符合 GDPR、CCPA 等法规；  
- **易用性**：提供 Web 控制台、Docker 部署方案及 Helm Chart 云原生支持。  

**使用方法：**  
1. **一键安装**：通过脚本快速部署；  
2. **Docker 启动**：需设置目录权限，支持单节点和分布式模式；  
3. **源码构建**：支持多架构编译（如 arm64）及版本自定义；  
4. **Kubernetes 部署**：通过 Helm Chart 安装。  

**注意事项：**  
- Docker 安装需确保目录权限和文件描述符限制（如 macOS 需执行 `ulimit -n 4096`）；  
- 默认控制台地址为 `http://localhost:9000`，账号密码为 `rustfsadmin`/`rustfsadmin`；  
- 支持 HTTPS 配置，需参考 TLS 文档。