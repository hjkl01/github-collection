
---
title: deep-chat
---

### [OvidijusParsiunas deep-chat](https://github.com/OvidijusParsiunas/deep-chat)

**核心内容总结：**  
Deep Chat 是一个高度可定制的 AI 聊天组件，可通过一行代码嵌入网站，支持连接 ChatGPT 等 20+ AI API 或自定义服务。  

**主要功能：**  
- 支持文件传输、摄像头拍照、麦克风录音、语音输入/输出（Speech to Text/Text to Speech）。  
- 支持 Markdown 和自定义元素渲染，提供动态模态框、专注模式等交互功能。  
- 可直接在浏览器运行模型（无需服务器），兼容 React/Vue/Svelte 等主流框架。  

**使用方法：**  
1. 通过 npm 安装（如 `npm install deep-chat`），React 项目需额外安装对应包。  
2. 在 HTML 中添加 `<deep-chat>` 标签并配置属性，如 `directConnection` 连接 API 或 `webModel` 启用本地模型。  
3. 通过服务器模板（Express/Flask/Go 等）快速搭建后端服务。  

**特性亮点：**  
- 提供 Playground 工具无需编码即可配置组件。  
- 支持全屏扩展视图，适配多平台部署（如 Vercel）。