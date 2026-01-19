
---
title: gotenberg
---

### [gotenberg gotenberg](https://github.com/gotenberg/gotenberg)  ![GitHub Repo stars](https://img.shields.io/github/stars/gotenberg/gotenberg?style=social)

**核心内容总结：**  
Gotenberg 是一个容器化 API，通过集成 Chromium 和 LibreOffice 工具，支持将 HTML、Markdown、Word、Excel 等多种文档格式转换为 PDF。  

**使用方法：**  
通过 Docker 命令快速启动服务：  
```
docker run --rm -p 3000:3000 gotenberg/gotenberg:8
```  
或使用 TheCodingMachine 镜像：  
```
docker run --rm -p 3000:3000 thecodingmachine/gotenberg:8
```  
启动后，API 通过 `http://localhost:3000` 访问。  

**主要特性：**  
- 支持多种文档格式转 PDF  
- 容器化部署，易于集成  
- 提供官方文档和在线演示功能