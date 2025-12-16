
---
title: etcd
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/etcd-io/etcd?style=social) ](https://github.com/etcd-io/etcd)
### [etcd-io etcd](https://github.com/etcd-io/etcd)

**项目核心内容总结：**

**功能**  
etcd 是一个分布式、可靠的键值存储系统，用于存储分布式系统的关键数据，基于 Raft 共识算法实现高可用性。

**主要特性**  
- **简单**：提供清晰的 gRPC API。  
- **安全**：支持自动 TLS 及可选客户端证书认证。  
- **高性能**：基准测试可达 10,000 次写入/秒。  
- **可靠**：通过 Raft 算法实现数据强一致性与故障恢复。  

**使用方法**  
1. **获取 etcd**：从 [发布页面](https://github.com/etcd-io/etcd/releases) 下载预编译二进制文件，或通过 `go get` 安装客户端库。  
2. **运行单节点**：执行 `etcd` 命令，默认监听 2379（客户端）和 2380（集群通信）端口。  
3. **操作数据**：使用 `etcdctl` 命令行工具，例如：  
   ```bash  
   etcdctl put mykey "value"  
   etcdctl get mykey  
   ```  
4. **本地集群**：通过 `goreman` 启动多节点集群（如 `infra1`, `infra2`, `infra3`）。  

**文档与资源**  
- 官方文档：[https://etcd.io/docs](https://etcd.io/docs)  
- Go 客户端 API：[https://godocs.io/go.etcd.io/etcd/v3](https://godocs.io/go.etcd.io/etcd/v3)  
- 社区支持：邮件组 [etcd-dev](https://groups.google.com/g/etcd-dev)、Slack 频道 `#sig-etcd`。  

**其他**  
- 许可证：Apache 2.0。  
- 贡献方式：参见 [CONTRIBUTING.md](CONTRIBUTING.md) 与 [roadmap](Documentation/contributor-guide/roadmap.md)。