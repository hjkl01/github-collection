
---
title: cnstd
---

### [breezedeus cnstd](https://github.com/breezedeus/cnstd)  ![GitHub Repo stars](https://img.shields.io/github/stars/breezedeus/cnstd?style=social)

CnSTD 是一个基于 Python 3 的场景文字检测（STD）工具包，支持中文、英文等多语言文字检测。项目基于 PyTorch 实现，支持 ONNX 推理加速，内置 DBNet、PP-OCR 等多种检测模型。

核心功能包括：
1. 场景文字检测（STD）：定位图片中的文字区域及坐标。
2. 数学公式检测（MFD）：识别行内及独立数学公式。
3. 版面分析（Layout Analysis）：识别文本、标题、图片、表格、公式等 10 种页面元素。

提供 Python API 和命令行工具，支持 CPU/GPU 环境，检测结果可配合 OCR 工具进行文字识别。