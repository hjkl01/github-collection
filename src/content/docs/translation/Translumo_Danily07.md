
---
title: Translumo
---

### [Danily07 Translumo](https://github.com/Danily07/Translumo)


**项目核心内容总结：**

Translumo 是一个先进的实时屏幕翻译工具，支持在 PC 游戏或其他应用程序中进行实时翻译。它通过结合多种 OCR 引擎（如 Windows OCR、Tesseract 和 EasyOCR）并使用机器学习模型选择最佳识别结果，实现高精度的文字识别。支持的翻译语言包括英语、俄语、日语、中文（简体）、韩语等，并可使用 DeepL、Google Translate 等多个翻译服务。

**使用方法：**

1. 打开设置（快捷键 Alt+G），选择 OCR 源语言和翻译目标语言。
2. 选择文本识别引擎（推荐使用 WindowsOCR）。
3. 定义捕获区域（快捷键 Alt+Q）。
4. 按下 ~ 键启动翻译。

**主要特性：**

- 高精度文本识别，支持多 OCR 引擎联合使用。
- 低延迟，优化系统资源使用。
- 支持多种翻译服务和多种语言。
- 可设置代理列表避免被翻译服务封禁。
- 适用于游戏窗口的无边框或窗口模式。

**系统要求：**

- 使用 Windows OCR 或 Tesseract 至少需要 Windows 10 2004 或 Windows 11，2GB RAM。
- 使用 EasyOCR 需要支持 CUDA 11.8 的 NVIDIA 显卡，8GB RAM 和 5GB 硬盘空间。

**构建要求：**

- 需要 Visual Studio 2022 和 .NET 8 SDK。
