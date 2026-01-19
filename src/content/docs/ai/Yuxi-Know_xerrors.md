
---
title: Yuxi-Know
---

### [xerrors Yuxi-Know](https://github.com/xerrors/Yuxi-Know)  ![GitHub Repo stars](https://img.shields.io/github/stars/xerrors/Yuxi-Know?style=social)

**项目总结：**

“语析”是一个基于大模型的知识库与知识图谱智能体开发平台，支持构建多智能体系统、文档处理、知识图谱生成与分析。主要功能包括：

- **核心功能**  
  - 支持RAG（检索增强生成）知识库，兼容多种文档格式（如Office、Markdown、压缩包等）；  
  - 提供知识图谱可视化工具，支持属性图谱导入与生成；  
  - 基于LangGraph v1框架开发智能体，支持中间件、子智能体、工具调用等；  
  - 包含知识库评估功能（支持Milvus类型库）、思维导图/示例问题生成等工具。

- **使用方法**  
  通过Git克隆代码后，执行初始化脚本并使用Docker启动项目，访问本地`http://localhost:5173`即可使用。

- **主要特性**  
  - 技术栈：Vue + FastAPI + Docker，支持暗色模式；  
  - 新增多模态模型支持、自定义模型配置、生产环境部署脚本；  
  - 优化异步操作、图谱可视化方式及文件管理逻辑；  
  - 移除Chroma支持，适配LangChain/LangGraph v1版本。

- **版本更新**  
  v0.4.3版本包含知识库评估、同名文件处理、UI优化等；v0.3.0全面适配LangGraph v1并升级文档解析功能。

**许可证**：MIT协议。