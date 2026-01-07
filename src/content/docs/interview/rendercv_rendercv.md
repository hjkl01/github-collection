
---
title: rendercv
---

### [rendercv rendercv](https://github.com/rendercv/rendercv)  ![GitHub Repo stars](https://img.shields.io/github/stars/rendercv/rendercv?style=social)

**项目核心内容总结：**

RenderCV 是一款用于生成学术和工程师简历（CV/简历）的工具，支持通过 YAML 文件编写内容并自动生成排版精美的 PDF。  

**功能与使用方法：**  
- 用 YAML 定义个人信息、教育经历、工作经历等，通过命令 `rendercv render 文件名.yaml` 生成 PDF。  
- 提供多种主题（如 Classic、Engineeringresumes 等），支持自定义设计参数（页边距、字体、颜色、对齐方式等）。  
- 安装方式：`pip install "rendercv[full]"`，创建新文件：`rendercv new "姓名"`。  

**主要特性：**  
1. **版本控制**：CV 内容以纯文本 YAML 存储，便于管理。  
2. **自动排版**：无需手动调整模板，生成 PDF 具备一致的间距和完美对齐。  
3. **设计灵活**：支持通过 YAML 配置主题、页面布局、颜色、字体等细节。  
4. **严格验证**：YAML 格式错误会明确提示，确保生成结果无误。  
5. **多语言支持**：通过 `locale` 字段配置语言（如英文、中文等）。  
6. **交互式填写**：提供 JSON Schema 用于 YAML 文件的自动补全和文档提示。