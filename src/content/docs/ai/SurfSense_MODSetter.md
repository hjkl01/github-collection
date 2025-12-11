
---
title: SurfSense
---

### [MODSetter SurfSense](https://github.com/MODSetter/SurfSense)

**项目核心内容总结：**  
SurfSense 是一款基于 AI 的研究代理工具，支持整合个人知识库与外部资源（如搜索引擎、Slack、Jira、Notion 等），提供多文件格式上传、智能搜索、对话交互、引用答案、本地 LLM 支持、团队协作管理、播客生成等功能。其核心特性包括：  
- **高级搜索**：结合向量相似度与全文检索（RRF 算法），支持多源数据精准查询。  
- **灵活部署**：提供云服务（无需安装）、Docker 快速启动、Docker Compose 生产部署及手动安装选项。  
- **技术栈**：后端基于 FastAPI、PostgreSQL（含向量搜索）、Redis；前端采用 Next.js、React、Tailwind CSS 等。  
- **扩展功能**：支持播客自动生成、文档智能分块与嵌入（Chonkie 库）、多用户权限管理等。  

**使用方法**：  
用户可通过 SurfSense Cloud 直接使用，或通过 Docker 命令快速本地部署，亦可配置 Docker Compose 实现生产级部署，手动安装需按文档配置依赖服务（如数据库、ETL 工具等）。