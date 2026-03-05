
---
title: monarch
---

### [meta-pytorch monarch](https://github.com/meta-pytorch/monarch)  ![GitHub Repo stars](https://img.shields.io/github/stars/meta-pytorch/monarch?style=social)

Monarch 是一个基于可扩展 Actor 消息传递机制的 PyTorch 分布式编程框架。它提供以下核心功能：

1. **远程 Actor 与可扩展消息传递**：Actor 可分组为 Mesh，支持向组内成员广播消息。
2. **基于监督树的容错机制**：Actor 和进程形成树结构，故障向上传播，提供默认错误处理和细粒度故障恢复。
3. **点对点 RDMA 传输**：支持注册任意 GPU 或 CPU 内存，基于 libibverbs 实现单向传输。
4. **分布式张量**：支持 Actor 操作跨进程分片的张量对象。

该项目通过简单的 Python API 以命令式方式描述进程和 Actor 的创建，目前处于实验开发阶段。