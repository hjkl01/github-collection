
---
title: MinerU
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/opendatalab/MinerU?style=social) ](https://github.com/opendatalab/MinerU)
### [opendatalab MinerU](https://github.com/opendatalab/MinerU)

**项目核心内容总结：**  
MinerU 是一个基于人工智能的高精度文档解析工具，支持从 PDF 等格式中提取文本、表格、代码块、手写文字、垂直文字等内容，并能识别文档结构（如标题、目录、列表）和化学公式。项目提供命令行工具和 API 接口，用户可通过安装依赖库后调用预训练模型实现文档内容提取。主要特性包括：  
1. **多场景识别**：支持复杂布局解析、表格结构识别、垂直文字及手写文字识别；  
2. **模型驱动**：基于深度学习模型（如 YOLO）实现内容布局分析和 OCR 识别；  
3. **开源工具链**：集成多个开源库（如 PaddleOCR、PDF-Extract-Kit）提升解析精度和效率。  

**使用方法**：安装依赖后，通过命令行或编程接口加载模型，输入文档文件路径，输出解析后的结构化数据（如 Markdown 格式）。