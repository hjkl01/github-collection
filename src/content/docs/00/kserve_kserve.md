
---
title: kserve
---

### [kserve kserve](https://github.com/kserve/kserve)  ![GitHub Repo stars](https://img.shields.io/github/stars/kserve/kserve?style=social)

**KServe 核心内容总结：**

**项目功能**  
KServe 是一个基于 Kubernetes 的标准化分布式 AI 推理平台，支持生成式 AI（如大语言模型）和预测式 AI（如 TensorFlow、PyTorch 等框架）的统一部署，提供多框架兼容、自动扩缩容、模型缓存优化等功能。

**使用方法**  
- **安装方式**：支持标准 Kubernetes 部署、Knative 无服务器部署、ModelMesh 高密度部署及本地快速安装。  
- **集成方式**：可通过 Kubeflow 安装作为扩展组件，或参考文档在 AWS/OpenShift 上部署。  
- **快速入门**：通过官方文档创建首个 InferenceService 实现模型部署。

**主要特性**  
1. **生成式 AI 优化**  
   - 支持 LLM 推理协议、GPU 加速、KV 缓存卸载至 CPU/磁盘、模型缓存机制。  
   - 提供基于请求的自动扩缩容及 Hugging Face 模型原生支持。  

2. **预测式 AI 能力**  
   - 支持多框架（TensorFlow/PyTorch/XGBoost 等）、智能请求路由、渐进式部署（金丝雀发布、流水线）。  
   - 内置模型解释、异常检测、成本优化（空闲时自动缩容至零）。  

3. **其他特性**  
   - 提供 InferenceGraph 高级部署、实时监控（漂移检测、日志分析）。  
   - 作为 CNCF 孵化项目，兼容 Kubeflow 生态，社区活跃度高。