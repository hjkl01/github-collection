
---
title: bentopdf
---

### [alam00000 bentopdf](https://github.com/alam00000/bentopdf)  ![GitHub Repo stars](https://img.shields.io/github/stars/alam00000/bentopdf?style=social)

**项目核心内容总结：**

**功能**  
BentoPDF 是一款基于浏览器的 PDF 工具集，支持创建、编辑、转换 PDF 文件，包括添加注释、合并/拆分 PDF、转换为 Word/Excel/PowerPoint 等格式，以及 HTML、Markdown 转 PDF 等功能。

**使用方法**  
1. **部署方式**：支持 Docker、npm 安装、Docker Compose 部署，提供“简单模式”（隐藏品牌内容，适合企业内部使用）。  
2. **运行方式**：通过命令行启动容器（如 `docker run -p 3000:8080 bentopdf`），或使用 `npm run dev` 启动本地开发服务器。  
3. **自定义配置**：支持通过 `BASE_URL` 参数部署到子路径，如 `/bentopdf/`。

**主要特性**  
- **客户端处理**：无需服务器依赖，使用 JavaScript 实现 PDF 操作（基于 PDFLib.js、PDF.js 等开源库）。  
- **格式支持**：支持 PDF/A 归档格式、Office 文档互转、Markdown/HTML 转 PDF 等。  
- **安全特性**：容器以非 root 用户运行，使用高端口（8080）避免权限风险。  
- **扩展性**：提供“简单模式”和“完整模式”，适配不同使用场景。  

**技术栈**  
基于 Vite、TypeScript、Tailwind CSS 构建，依赖 PDFLib.js、PDF.js 等开源工具实现核心功能。