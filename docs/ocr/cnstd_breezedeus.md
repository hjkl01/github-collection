### [breezedeus cnstd](https://github.com/breezedeus/cnstd)  ![GitHub Repo stars](https://img.shields.io/github/stars/breezedeus/cnstd?style=social)

CnSTD 是一个基于 Python 3 的场景文字检测（STD）工具包，主要功能如下：

1. **场景文字检测**：支持中文、英文等多种语言，内置基于 DBNet、PaddleOCR 及 YOLO 等架构的预训练模型，支持角度文本框检测，可配合 cnocr 工具进行文字识别。
2. **数学公式检测（MFD）**：识别图片中的行内公式（embedding）与独立行公式（isolated）。
3. **版面分析（Layout Analysis）**：识别图片中的正文、标题、图片、表格、页眉页脚等 10 种版面元素。

项目支持 PyTorch 和 ONNX 推理后端，提供命令行工具用于预测、训练及模型管理，安装后自动下载并缓存模型，轻量易用。