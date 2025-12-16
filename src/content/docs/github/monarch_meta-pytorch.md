
---
title: monarch
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/meta-pytorch/monarch?style=social) ](https://github.com/meta-pytorch/monarch)
### [meta-pytorch monarch](https://github.com/meta-pytorch/monarch)

**Monarch** 是一个基于 PyTorch 的分布式编程框架，通过可扩展的 actor 消息传递机制实现分布式计算。其核心功能包括：

1. **远程 actor 分组与通信**  
   支持将 actor 分组为“mesh”并广播消息，实现跨进程通信。

2. **故障恢复机制**  
   通过监督树（supervision tree）实现故障传播与恢复，提供默认错误处理和细粒度恢复能力。

3. **高性能 RDMA 传输**  
   支持 GPU/CPU 内存的点对点 RDMA 传输（基于 libibverbs），降低通信开销。

4. **分布式张量支持**  
   允许 actor 操作跨进程分片的张量对象。

**使用方法**  
通过 Python API 定义 actor 和进程，示例如下：  
- 使用 `this_host().spawn_procs()` 创建进程；  
- 定义 actor 类并注册接口（`@endpoint`）；  
- 调用 `.call()` 触发远程方法并等待结果。

**主要特性**  
- 支持 GPU/CPU 内存的高效 RDMA 传输；  
- 提供分布式张量分片能力；  
- 基于监督树的故障恢复机制；  
- 简洁的 Python API 用于进程/actor 管理。

**注意事项**  
- 当前为实验性项目，API 可能变更，建议在贡献前讨论；  
- 安装需依赖 libibverbs、libmlx5 等库，且 PyTorch 版本需匹配；  
- 支持通过 `pip` 安装（稳定版或 nightly 版），或从源码构建（需 CUDA/Clang 等环境）。