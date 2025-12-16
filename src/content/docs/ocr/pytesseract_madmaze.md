
---
title: pytesseract
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/madmaze/pytesseract?style=social) ](https://github.com/madmaze/pytesseract)
### [madmaze pytesseract](https://github.com/madmaze/pytesseract)

**项目核心内容总结：**

Python Tesseract 是基于 Google Tesseract-OCR 引擎的 Python 光学字符识别（OCR）工具，用于从图像中提取文字。支持多种图像格式（如 JPEG、PNG、BMP 等），可作为库或独立脚本使用，输出识别结果或保存为 PDF/HOCR 等格式。

**功能与使用方法：**  
1. **基本用法**：通过 `image_to_string` 函数识别图像文字，支持指定语言（如 `lang='fra'` 识别法语）。  
2. **高级功能**：提供边界框（`image_to_boxes`）、详细数据（`image_to_data`）、PDF 输出（`image_to_pdf_or_hocr`）、ALTO XML 等多种输出类型。  
3. **OpenCV 支持**：兼容 OpenCV 图像，需将 BGR 格式转换为 RGB。  
4. **配置自定义**：可通过 `config` 参数设置 Tesseract 配置（如 `--psm 6`），或指定 `tessdata` 路径解决数据文件缺失问题。

**主要特性：**  
- 支持多语言识别（需安装对应语言包）。  
- 批量处理图像文件（通过文件路径列表）。  
- 超时控制（防止长时间无响应）。  
- 多输出格式（文本、PDF、HOCR、XML 等）。  
- 兼容 Pillow 和 OpenCV 图像处理库。

**安装要求：**  
需 Python 3.6+、Pillow 库及 Tesseract-OCR 引擎。可通过 `pip install pytesseract` 或 Conda 安装。若 Tesseract 未加入系统路径，需手动设置 `pytesseract.tesseract_cmd` 指向可执行文件路径。