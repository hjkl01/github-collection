
---
title: AgentOCR
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/AgentMaker/AgentOCR?style=social) ](https://github.com/AgentMaker/AgentOCR)
### [AgentMaker AgentOCR](https://github.com/AgentMaker/AgentOCR)

AgentMaker是一个基于PaddleOCR的多功能OCR工具，支持多语言文字识别（中、英、法、德、韩、日等）及中国车牌识别。核心功能包括：  
1. **多语言识别**：覆盖中文（简繁）、英文、韩文等12种语言，支持不同语言模型的灵活调用；  
2. **车牌识别**：集成专用检测识别系统；  
3. **模型优化**：基于PaddleOCR v2模型，提供字典优化和高性能识别。  

**使用方法**：通过安装依赖后，初始化API对象并调用`recognize`方法，支持传入图片路径或Base64编码数据。  

**主要特性**：轻量级设计、多平台兼容、支持ONNX模型部署，未来将扩展结构识别、GUI界面及模型转换工具。