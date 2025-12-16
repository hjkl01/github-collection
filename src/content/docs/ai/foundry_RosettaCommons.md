
---
title: foundry
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/RosettaCommons/foundry?style=social) ](https://github.com/RosettaCommons/foundry)
### [RosettaCommons foundry](https://github.com/RosettaCommons/foundry)

**核心内容总结：**  
Foundry 是一个用于蛋白质设计的工具平台，整合了多种模型（如 RFD3、RF3、ProteinMPNN）用于蛋白质设计、逆折叠和结构预测。项目依赖 AtomWorks 框架处理生物分子结构。  

**使用方法：**  
1. 安装：`pip install "rc-foundry[all]"`  
2. 下载模型权重：`foundry install base-models --checkpoint-dir <路径>`  
3. 提供 Colab 教程和示例代码（如 `examples/all.ipynb`）支持快速上手。  

**主要特性：**  
- 支持多种模型（RFD3、RF3、MPNN）的训练与推理；  
- 提供模型注册表查询（`foundry list-available`）和本地安装状态检查（`foundry list-installed`）；  
- 开发者友好：支持新增模型模块、代码格式化（pre-commit）及可编辑模式开发；  
- 文档完善，包含模型专用说明（如 `models/rfd3/README.md`）和引用文献。