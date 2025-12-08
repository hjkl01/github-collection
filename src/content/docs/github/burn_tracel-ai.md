
---
title: burn
---

### [tracel-ai burn](https://github.com/tracel-ai/burn)

**Burn项目核心内容总结：**

**功能**  
Burn是一个基于Rust的深度学习框架，支持模型训练与推理、自定义操作开发、跨平台部署（如WebAssembly），并兼容ONNX和PyTorch模型导入。提供多种示例（如图像分类、文本生成、GAN等）及预训练模型，适用于计算机视觉、自然语言处理等任务。

**使用方法**  
- 提供详细教程和示例代码（如MNIST训练、自定义数据集处理）。  
- 支持通过`Learner`进行训练，或自定义训练循环。  
- 可导入ONNX/PyTorch模型进行推理，或导出为自定义格式。  
- 社区提供模型库（如[tracel-ai/models](https://github.com/tracel-ai/models)）和活跃的Discord讨论群。

**主要特性**  
- **高性能**：利用Rust零成本抽象和内存控制优化计算效率。  
- **模块化设计**：支持自定义层、数据集、训练逻辑和WGPU内核。  
- **跨平台**：支持WebAssembly部署，适用于浏览器端应用。  
- **易用性**：提供自动微分、高级API及与主流框架的兼容性。  
- **社区支持**：活跃的开发者社区，持续更新文档和模型示例。

**注意事项**  
- 从0.14.0版本起，`TensorData`替代旧版`Data`结构，加载旧版本模型需使用兼容版本（<=0.16.0）并启用`record-backward-compat`功能标志。