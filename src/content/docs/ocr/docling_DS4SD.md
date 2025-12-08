
---
title: docling
---

### [DS4SD docling](https://github.com/DS4SD/docling)

**项目核心内容总结：**  

**功能**  
Docling 是一个文档处理工具，支持 PDF、DOCX、PPTX、XLSX、HTML、音频（WAV/MP3）、图像（PNG/TIFF/JPEG）等多种格式的解析。具备高级 PDF 理解能力，包括页面布局、表格结构、代码、公式识别，以及图像分类。提供统一的文档表示格式（`DoclingDocument`），支持导出为 Markdown、HTML、JSON 等格式，并兼容本地执行环境（适用于敏感数据场景）。  

**主要特性**  
- 支持 OCR 解析扫描件及图像；  
- 集成视觉语言模型（如 GraniteDocling）和音频识别模型；  
- 提供 MCP 服务器接口，支持与 AI 代理系统连接；  
- 包含命令行工具（CLI），支持快速转换；  
- 支持结构化信息提取（Beta 阶段）及新布局模型（Heron）提升 PDF 解析效率；  
- 与 LangChain、LlamaIndex 等主流 AI 框架兼容。  

**使用方法**  
通过 Python API 调用 `DocumentConverter.convert()` 方法，或使用 CLI 命令（如 `docling [文件路径]`）处理文档。支持指定视觉语言模型（如 `--vlm-model granite_docling`）进行高级解析。  

**安装**  
使用 `pip install docling` 安装，兼容 macOS、Linux、Windows 及 ARM64 架构。  

**文档与资源**  
提供详细文档、示例和集成指南，支持扩展开发。