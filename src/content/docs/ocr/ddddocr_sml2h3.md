
---
title: ddddocr
---

### [sml2h3 ddddocr](https://github.com/sml2h3/ddddocr)  ![GitHub Repo stars](https://img.shields.io/github/stars/sml2h3/ddddocr?style=social)

DdddOcr 是一个通用的离线本地验证码识别 Python SDK。

**核心功能：**
1.  **文字识别（OCR）**：支持数字、字母、中文及特殊字符识别，提供概率输出、自定义字符范围、颜色过滤及透明 PNG 修复功能。
2.  **目标检测**：检测图片中目标主体的边界框坐标。
3.  **滑块验证处理**：提供边缘匹配和图像差异比较两种算法，用于识别滑块验证码缺口位置。
4.  **自定义模型**：支持导入外部训练的 ONNX 模型及字符集文件进行识别。
5.  **API 服务**：内置 RESTful API 服务，支持通过命令行启动或 Docker 部署，提供 HTTP 接口调用。

**环境与支持：**
兼容 Windows、Linux、macOS 系统，支持 CPU 及 GPU 加速，提供批量处理与多线程优化方案。