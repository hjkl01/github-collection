
---
title: kserve
---

### [kserve kserve](https://github.com/kserve/kserve)  ![GitHub Repo stars](https://img.shields.io/github/stars/kserve/kserve?style=social)

KServe 是一个基于 Kubernetes 的标准化分布式 AI 推理平台，由 CNCF 孵化，旨在统一生成式和预测式 AI 的推理部署。

核心功能：
- **生成式 AI**：支持 vLLM 等优化后端，提供 OpenAI 兼容协议、GPU 加速、模型缓存、KV 缓存卸载、请求式自动扩缩容及 Hugging Face 原生支持。
- **预测式 AI**：支持 TensorFlow、PyTorch 等多框架，具备智能路由、金丝雀发布、推理管道集成、自动扩缩容（支持零扩展）、模型可解释性及高级监控（漂移/异常检测）。
- **部署**：支持标准 Kubernetes、Knative 无服务器、ModelMesh 及 Kubeflow 集成等多种安装模式。