
---
title: computer-use-preview
---

### [google-gemini computer-use-preview](https://github.com/google-gemini/computer-use-preview)  ![GitHub Repo stars](https://img.shields.io/github/stars/google-gemini/computer-use-preview?style=social)

**项目核心内容总结：**  
该项目是一个基于浏览器的代理工具，通过自然语言指令控制浏览器执行任务（如访问网站、输入搜索内容等），支持使用Gemini API或Vertex AI模型。  

**使用方法：**  
1. **安装**：克隆仓库、创建虚拟环境、安装依赖（包括Playwright及浏览器）。  
2. **配置**：根据选择的模型（Gemini API或Vertex AI），设置对应环境变量（API密钥、项目ID等）。  
3. **运行**：通过`main.py`脚本执行指令，支持两种环境（本地Playwright或Browserbase），可指定初始URL及调试参数（如鼠标高亮）。  

**主要特性：**  
- 支持本地Playwright（控制Chrome浏览器）或Browserbase（云端浏览器）环境。  
- 提供CLI命令行接口，通过自然语言指令控制浏览器操作。  
- 可调试功能（如截图鼠标位置）。  
- 已知问题：Playwright在部分系统上无法处理下拉菜单，可切换至Browserbase或使用脚本修复。