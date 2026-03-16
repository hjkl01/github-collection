### [karpathy char-rnn](https://github.com/karpathy/char-rnn)  ![GitHub Repo stars](https://img.shields.io/github/stars/karpathy/char-rnn?style=social)

该项目基于 Lua/Torch 框架实现了多层 RNN（含 LSTM/GRU），用于训练字符级语言模型。输入文本文件后，模型学习预测序列中的下一个字符，从而生成与原始训练数据风格相似的文本。项目支持 CPU 及 GPU 加速，提供训练与采样脚本，具备模型检查点管理、超参数调节（网络规模、温度、预热文本）及验证损失监控等核心功能。