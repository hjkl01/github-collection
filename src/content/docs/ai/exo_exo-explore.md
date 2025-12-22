
---
title: exo
---

### [exo-explore exo](https://github.com/exo-explore/exo)  ![GitHub Repo stars](https://img.shields.io/github/stars/exo-explore/exo?style=social)

**项目核心内容总结：**

**功能**  
exo 是一个可在家庭设备上运行的 AI 集群系统，支持通过自动设备发现、RDMA 技术及拓扑感知并行计算，实现多设备协同运行大模型，并显著降低延迟。

**主要特性**  
- 自动设备发现：设备间无需手动配置即可互联。  
- RDMA over Thunderbolt：支持 Thunderbolt 5 的 RDMA 技术，降低设备间通信延迟。  
- 拓扑感知自动并行：根据设备资源和网络状况自动优化模型分布。  
- 张量并行：支持多设备模型分片，提升运算速度（如 2 设备 1.8 倍加速）。  
- MLX 支持：基于 MLX 框架实现推理和分布式通信。

**使用方法**  
1. **从源码运行**（Mac/Linux）：克隆仓库、构建仪表盘、执行 `uv run exo`，访问 `http://localhost:52415`。  
2. **macOS 应用**：下载安装包（需 macOS 26.2 及以上），后台运行。  
3. **API 调用**：通过 API 创建模型实例、发送请求及删除实例（示例包含 curl 命令）。  

**硬件支持**  
- macOS 使用 GPU，Linux 当前仅支持 CPU，未来计划扩展其他硬件平台。