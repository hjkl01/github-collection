### [nubskr walrus](https://github.com/nubskr/walrus)  ![GitHub Repo stars](https://img.shields.io/github/stars/nubskr/walrus?style=social)

Walrus 是一个基于高性能日志存储引擎构建的分布式消息流平台。

1. **分布式架构**：基于 Raft 共识维护集群元数据，支持 3+ 节点，自动进行领导权轮换与分片负载均衡。
2. **数据一致性**：采用租约写入封锁机制防止脑裂，确保写入安全；支持密封分段读取历史数据。
3. **高性能**：底层存储支持 Linux io_uring，提供高吞吐量写入与读取能力。
4. **接入方式**：提供简单的 TCP 文本协议、交互式 CLI 命令行及可嵌入的 Rust 存储引擎库。
5. **正确性验证**：包含 TLA+ 形式化规格说明，验证分布式数据平面的不变性与活性。