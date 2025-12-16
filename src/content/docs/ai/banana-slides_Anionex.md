
---
title: banana-slides
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/Anionex/banana-slides?style=social) ](https://github.com/Anionex/banana-slides)
### [Anionex banana-slides](https://github.com/Anionex/banana-slides)

**项目核心内容总结：**

1. **项目功能**  
   - AI驱动的PPT生成工具，支持通过大纲、文本输入或文件导入（如Markdown、文档）自动生成幻灯片内容。  
   - 提供大纲编辑、详细描述输入、实时预览、素材库（图片/模板）调用、历史版本管理等功能。  
   - 支持导出为PPTX/PDF格式，兼容多种设备和平台。

2. **主要特性**  
   - 多种内容生成方式：支持通过自然语言指令、大纲结构或文件解析生成幻灯片。  
   - 灵活编辑与定制：可调整大纲层级、页面描述，集成素材库（自定义模板、参考文件）。  
   - AI能力：基于Google Gemini API实现内容生成与优化。  
   - 异步处理：支持后台任务管理，提升大文件或复杂项目的处理效率。

3. **使用方法**  
   - **安装方式**：  
     - 通过Docker Compose一键部署（需配置环境变量如`GOOGLE_API_KEY`）。  
     - 手动安装：分别构建前端（React + Vite）和后端（Flask + Python 3.10+），启动前后端服务。  
   - **操作流程**：  
     - 创建项目，输入大纲或上传文件，AI生成初稿；  
     - 编辑页面描述，调用素材库优化内容；  
     - 预览并导出为PPTX/PDF。

4. **技术架构**  
   - 前端：React 18 + TypeScript + Tailwind CSS；后端：Flask 3.0 + SQLite + Google Gemini API。  
   - 核心依赖：PPT处理（python-pptx）、图片处理（Pillow）、异步任务（ThreadPoolExecutor）。