
---
title: monarch
---

### [meta-pytorch monarch](https://github.com/meta-pytorch/monarch)  ![GitHub Repo stars](https://img.shields.io/github/stars/meta-pytorch/monarch?style=social)

Monarch 是一个基于可扩展演员消息传递的 PyTorch 分布式编程框架。核心功能包括：

1. **远程演员与消息传递**：支持将演员分组为集合（meshes），并可向所有成员广播消息。
2. **故障容错**：通过监督树结构实现进程故障传播及细粒度恢复。
3. **点对点 RDMA 传输**：支持 GPU 或 CPU 内存的廉价注册及基于 libibverbs 的单侧传输。
4. **分布式张量**：支持演员操作跨进程分片的张量对象。

项目提供简单的 Python API 以命令式方式定义进程和演员，当前处于实验开发阶段。