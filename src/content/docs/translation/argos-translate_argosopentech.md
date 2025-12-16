
---
title: argos-translate
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/argosopentech/argos-translate?style=social) ](https://github.com/argosopentech/argos-translate)
### [argosopentech argos-translate](https://github.com/argosopentech/argos-translate)

**Argos Translate 核心内容总结：**

**项目功能**  
Argos Translate 是一个开源的离线翻译库，基于 Python 实现，支持通过 Python 库、命令行工具或图形界面（GUI）进行翻译。其核心功能包括：  
- 使用 OpenNMT 框架实现高质量翻译；  
- 支持安装语言模型包（`.argosmodel` 格式），实现多语言翻译；  
- 自动通过中间语言进行翻译（如通过英语中转实现西班牙语→法语翻译）；  
- 集成 LibreTranslate 作为 API 和网页应用。  

**使用方法**  
1. **Python 安装**：通过 `pip install argostranslate` 安装核心库，`pip install argostranslategui` 安装 GUI。  
2. **命令行使用**：通过 `argospm` 安装语言包（如 `argospm install translate-en_de`），使用 `argos-translate` 命令执行翻译。  
3. **代码示例**：Python 中调用 `argostranslate.translate.translate()` 实现翻译，需先下载对应语言模型包。  
4. **API 调用**：通过 LibreTranslate 提供的 REST API 实现翻译（如 JavaScript 中发送 POST 请求）。  

**主要特性**  
- **多语言支持**：涵盖阿拉伯语、英语、中文、法语、西班牙语等 30+ 语言（支持扩展）；  
- **离线运行**：无需网络依赖，适合本地部署；  
- **GPU 加速**：通过设置 `ARGOS_DEVICE_TYPE=cuda` 启用 GPU 加速翻译；  
- **扩展功能**：支持 HTML/文件翻译（依赖 `translate-html` 和 `argos-translate-files` 库）；  
- **模型管理**：提供模型包索引（[argospm-index](https://github.com/argosopentech/argospm-index)），支持 P2P 下载和自定义训练。