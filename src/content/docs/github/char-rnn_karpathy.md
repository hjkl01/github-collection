
---
title: char-rnn
---

### [karpathy char-rnn](https://github.com/karpathy/char-rnn)

**项目核心内容总结：**

1. **项目功能**  
   实现基于RNN/LSTM/GRU的字符级语言模型，通过训练文本文件学习预测字符序列，生成类似训练数据的新文本。支持多层网络结构、GPU加速、模型检查点保存与加载。

2. **使用方法**  
   - **数据准备**：将输入文本文件放入`data/`目录，格式为`data/文件夹/input.txt`。  
   - **训练**：使用`train.lua`脚本，指定数据路径、网络参数（如`-rnn_size`、`-num_layers`）及GPU/CPU模式（如`-gpuid -1`）。训练时会定期保存验证损失值的检查点文件（如`lm_lstm_epochX_lossY.t7`）。  
   - **生成文本**：通过`sample.lua`加载检查点文件，调整生成长度（`-length`）、温度（`-temperature`）及起始文本（`-primetext`）参数。若需CPU模式生成，需先用脚本转换GPU检查点为CPU格式。  

3. **主要特性**  
   - 支持LSTM、GRU及多层网络结构。  
   - 提供模型检查点、验证损失监控、参数调整（如dropout、序列长度）。  
   - 可通过调整`rnn_size`、`num_layers`等参数优化模型性能，建议根据数据量匹配模型规模。  
   - 提供多种优化策略（如调整温度控制生成多样性、使用验证损失选择最佳模型）。  

**注意事项**：需安装Torch及依赖库（如nngraph、optim），GPU训练需额外安装cutorch/cunn。