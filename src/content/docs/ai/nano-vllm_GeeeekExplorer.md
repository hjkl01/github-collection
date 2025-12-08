
---
title: nano-vllm
---

### [GeeeekExplorer nano-vllm](https://github.com/GeeeekExplorer/nano-vllm)

**项目核心内容总结：**  
Nano-vLLM 是一个从零开始构建的轻量级 vLLM 实现，具备以下特性：  
- **高效推理**：离线推理速度与 vLLM 相当，吞吐量更高（测试显示 1434 tokens/s）。  
- **代码简洁**：约 1200 行 Python 代码，结构清晰易读。  
- **优化技术**：集成前缀缓存、张量并行、CUDA 图等加速方案。  

**使用方法**：  
1. **安装**：通过 `pip install git+https://github.com/GeeeekExplorer/nano-vllm.git` 安装。  
2. **模型下载**：使用 `huggingface-cli` 下载模型权重（如 Qwen3-0.6B）。  
3. **调用示例**：通过 `LLM.generate` 接口生成文本，支持与 vLLM 兼容的参数配置。  

**性能**：在 RTX 4070（8GB）上测试，处理 256 个请求时，Nano-vLLM 吞吐量比 vLLM 提高约 5.3%。