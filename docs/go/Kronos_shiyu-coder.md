### [shiyu-coder Kronos](https://github.com/shiyu-coder/Kronos)  ![GitHub Repo stars](https://img.shields.io/github/stars/shiyu-coder/Kronos?style=social)

Kronos 是首个面向金融 K 线序列的开源基础模型，基于 45 多个全球交易所数据训练。项目采用专用 Tokenizer 将 OHLCV 数据量化为离散 Token，结合自回归 Transformer 预训练，实现统一的量化任务建模。主要功能包括提供 Mini 至 Base 等多种参数量级的预训练模型，通过预测器接口支持单条及批量 K 线数据预测，并支持在自定义数据（如 A 股）上进行模型微调及回测。模型托管于 Hugging Face，采用 MIT 协议。