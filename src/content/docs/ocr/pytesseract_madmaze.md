
---
title: pytesseract
---

### [madmaze pytesseract](https://github.com/madmaze/pytesseract)  ![GitHub Repo stars](https://img.shields.io/github/stars/madmaze/pytesseract?style=social)

Python-tesseract 是一个基于 Google Tesseract-OCR 引擎的 Python 光学字符识别（OCR）工具，用于识别和读取嵌入图像中的文本。它支持 Pillow 和 Leptonica 库支持的多种图片格式（如 jpeg, png, gif, bmp, tiff）。

核心功能包括：
1. **文本识别**：支持多语言识别、自定义配置（如 OEM/PSM）、批量处理及超时控制。
2. **详细信息提取**：获取字符边界框、置信度、行列页码、图像方向及脚本信息。
3. **多格式输出**：支持生成文本、可搜索 PDF、HOCR、ALTO XML 或 TSV 格式，支持多种格式一次性调用输出。
4. **兼容性**：兼容 PIL、OpenCV 图像及 NumPy 数组，并提供命令行接口（CLI）。

使用前需安装 Python 3.6+、Pillow 及 Tesseract-OCR 引擎。