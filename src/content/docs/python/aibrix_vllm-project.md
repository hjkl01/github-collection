
---
title: aibrix
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/vllm-project/aibrix?style=social) ](https://github.com/vllm-project/aibrix)
### [vllm-project aibrix](https://github.com/vllm-project/aibrix)

**AIBrix核心内容总结**  
AIBrix是一个开源的云原生项目，提供构建可扩展的生成式AI（GenAI）推理基础设施的工具，专为企业的大型语言模型（LLM）部署优化。  

**主要功能**  
- **高效推理管理**：支持高密度LoRA模型适配、多模型流量路由、动态资源自动扩展。  
- **分布式架构**：实现跨节点的分布式推理与KV缓存复用，提升大规模负载处理能力。  
- **成本优化**：支持异构GPU混合推理，结合SLO保障降低硬件成本。  
- **稳定性保障**：内置GPU硬件故障主动检测机制。  

**使用方法**  
1. 克隆代码库并执行`kubectl`命令安装依赖与组件（本地测试或稳定版本）。  
2. 通过`config/dependency`和`config/default`目录配置部署。  
3. 稳定版本可直接下载预发布YAML文件进行安装。  

**核心特性**  
- 统一AI运行时（支持模型下载与指标标准化）  
- LLM应用定制化自动扩缩容  
- 跨引擎分布式KV缓存技术  
- 针对Kubernetes的LLM感知负载均衡方案