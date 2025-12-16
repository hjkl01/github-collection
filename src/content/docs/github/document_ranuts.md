
---
title: document
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/ranuts/document?style=social) ](https://github.com/ranuts/document)
### [ranuts document](https://github.com/ranuts/document)

**项目核心内容总结：**  
OnlyOffice Web 是一个基于浏览器的本地文档编辑器，支持在无服务器处理的情况下直接编辑 DOCX、XLSX、PPTX 等格式文件，保障隐私与安全。  

**主要功能与特性：**  
- **隐私保护**：所有文档处理在浏览器本地完成，不上传服务器。  
- **多格式支持**：兼容 DOCX、XLSX、PPTX、CSV 等多种文档格式。  
- **实时编辑**：提供流畅的实时协作编辑体验。  
- **无需服务器**：纯前端实现，无需后端支持。  
- **多语言界面**：支持中英文切换。  
- **URL 直接加载**：可通过 URL 参数（如 `?src=远程地址`）直接打开远程文档。  

**使用方法：**  
1. 访问 [在线编辑器](https://ranuts.github.io/document/)，上传文件或通过 URL 参数加载文档。  
2. 使用 Docker 部署：`docker run -d --name document -p 8080:8080 ghcr.io/ranui/document:latest`。  
3. 本地开发：克隆仓库后执行 `npm install` 和 `npm run dev`。  

**注意事项：**  
- 使用远程 URL 时需确保服务器支持 CORS。  
- 项目未包含专有字体（如 Arial），需手动将字体文件放入 `public/fonts/` 目录并按索引命名以启用。