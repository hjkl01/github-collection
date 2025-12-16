
---
title: EasyOCR
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/JaidedAI/EasyOCR?style=social) ](https://github.com/JaidedAI/EasyOCR)
### [JaidedAI EasyOCR](https://github.com/JaidedAI/EasyOCR)

**项目功能**  
EasyOCR 是一个支持 80+ 种语言（含中文、英文、阿拉伯文、俄文等）的 OCR 工具，可识别图像中的文字并返回边界框、文本内容及置信度。  

**使用方法**  
1. 安装：`pip install easyocr`（或开发版 `pip install git+https://github.com/JaidedAI/EasyOCR.git`）。  
2. 代码示例：  
   ```python  
   import easyocr  
   reader = easyocr.Reader(['ch_sim', 'en'])  # 加载模型  
   result = reader.readtext('image.jpg')  # 返回 [(边界框, 文本, 置信度), ...]  
   ```  
3. 支持输入类型：文件路径、OpenCV 图像、字节流或图片 URL。  
4. 可通过 `detail=0` 简化输出为纯文本列表。  

**主要特性**  
- 自动下载模型权重，支持 CPU/GPU 运行（`gpu=False` 切换 CPU）。  
- 提供命令行工具，支持多语言混合识别（如 `easyocr -l ch_sim en -f image.jpg`）。  
- 支持训练自定义模型（识别模型和检测模型）。  
- 基于 PyTorch，融合 CRAFT（文本检测）和 CRNN（文本识别）技术。  
- 社区可贡献新语言（需提供字符集和词典文件）。