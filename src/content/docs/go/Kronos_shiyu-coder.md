
---
title: Kronos
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/shiyu-coder/Kronos?style=social) ](https://github.com/shiyu-coder/Kronos)
### [shiyu-coder Kronos](https://github.com/shiyu-coder/Kronos)

**项目核心内容总结：**  
Kronos 是一个面向金融市场的基础模型，用于时间序列预测（如股票价格预测）。其功能包括：  
1. **预测**：提供基于金融数据的预测能力，支持单资产和多资产批量预测。  
2. **微调**：支持在自定义数据集（如A股市场）上微调模型，包含数据预处理、模型训练和回测流程。  
3. **回测**：集成Qlib框架，可对微调后的模型进行策略回测，评估预测效果。  

**使用方法**：  
- 安装依赖库（如Qlib、PyTorch）。  
- 准备数据（使用Qlib处理A股市场数据）。  
- 训练模型：分两阶段微调（Tokenizer和Predictor），支持多GPU加速。  
- 回测：加载微调模型，生成预测信号并执行简单策略回测。  

**主要特性**：  
- 支持多GPU训练和批量预测。  
- 提供完整示例代码（预测、微调、回测）。  
- 集成Qlib数据处理框架，简化金融数据准备。  
- 适用于金融市场时间序列建模与量化策略研究。