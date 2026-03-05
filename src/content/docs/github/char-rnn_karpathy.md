
---
title: char-rnn
---

### [karpathy char-rnn](https://github.com/karpathy/char-rnn)  ![GitHub Repo stars](https://img.shields.io/github/stars/karpathy/char-rnn?style=social)

本项目基于多层循环神经网络（RNN、LSTM 和 GRU）实现字符级语言模型。它接受文本文件作为输入，训练模型预测序列中的下一个字符，并据此生成与训练数据风格相似的新文本。

主要功能包括：
1. **模型训练**：使用 Lua/Torch 编写，支持 CPU/GPU 加速，可配置网络层数、大小及 Batch 设置，支持模型检查点保存与恢复。
2. **文本生成**：基于训练好的模型检查点进行采样，支持自定义生成长度、温度参数（控制输出多样性）及起始文本引导。
3. **数据与调优**：支持自定义数据集预处理，并提供关于监控训练/验证损失、调整模型规模及防止过拟合的实用建议。