
---
title: screenshot-to-code
---

### [abi screenshot-to-code](https://github.com/abi/screenshot-to-code)

**核心内容总结：**  
该项目是一个基于AI的工具，可将截图、线框图或Figma设计转换为多种技术栈的代码（如HTML+Tailwind、React+Tailwind、Bootstrap等），并支持Claude Sonnet 3.7、GPT-4o等模型。其主要特性包括：  
1. **功能**：支持截图转代码、视频录制转原型（实验性功能），并提供多种AI模型结果对比。  
2. **使用方法**：需配置OpenAI或Anthropic API密钥，通过FastAPI后端和React/Vite前端运行，支持Docker部署。  
3. **技术栈**：兼容主流前端框架（React/Vue/Bootstrap等）及Tailwind，支持DALL-E 3等图像生成模型。  
4. **扩展性**：提供本地开发模式（需手动安装依赖）和模拟模式（节省API调用）。  

**注意事项**：需注意API密钥配置、UTF-8编码问题及后端与前端的连接设置。