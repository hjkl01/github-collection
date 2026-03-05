
---
title: Kronos
---

### [shiyu-coder Kronos](https://github.com/shiyu-coder/Kronos)  ![GitHub Repo stars](https://img.shields.io/github/stars/shiyu-coder/Kronos?style=social)

Kronos 是首个面向金融 K 线序列的开源基础模型，基于 45 多个全球交易所数据训练。它采用专用 Tokenizer 将多维 OHLCV 数据量化为分层离散 Token，并结合自回归 Transformer 架构进行预训练。项目核心功能包括金融时间序列预测（支持批量预测与概率采样）、针对特定市场（如 A 股）的模型微调、提供不同参数量级的预训练模型，以及包含数据预处理、预测结果可视化与回测评估的完整代码示例。