### [kserve kserve](https://github.com/kserve/kserve)  ![GitHub Repo stars](https://img.shields.io/github/stars/kserve/kserve?style=social)

KServe 是一个基于 Kubernetes 的标准化分布式 AI 推理平台，由 CNCF 孵化，统一支持生成式和预测式 AI 的可扩展部署。

功能特性：
1. 生成式 AI：支持 vLLM/llm-d 优化后端，提供 GPU 加速、模型缓存、KV Cache 卸载、请求级自动扩缩容及 OpenAI 兼容协议，原生适配 Hugging Face。
2. 预测式 AI：支持 TensorFlow、PyTorch 等多框架，具备智能路由、Canary 部署、InferenceGraph 流水线、模型可解释性、高级监控及缩容到零成本优化。
3. 部署支持：提供 Kubernetes 标准、Knative Serverless 及 ModelMesh 安装选项，并可集成至 Kubeflow。