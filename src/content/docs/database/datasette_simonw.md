
---
title: datasette
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/simonw/datasette?style=social) ](https://github.com/simonw/datasette)
### [simonw datasette](https://github.com/simonw/datasette)

**Datasette核心内容总结：**  
Datasette是一款开源工具，用于探索和发布各类数据（如SQLite数据库），可生成交互式网页和配套API。主要面向数据记者、研究人员、档案管理者等需要共享数据的用户。  

**功能与特性：**  
1. **数据探索与发布**：支持SQLite等数据库，自动生成网页界面和API，可浏览数据、执行SQL查询。  
2. **元数据支持**：通过`metadata.json`文件添加数据来源、许可证等信息，展示在网页和API响应中。  
3. **快速部署**：提供`datasette publish`命令，一键将数据库部署至Heroku或Google Cloud Run。  
4. **跨平台运行**：支持本地运行（Python 3.8+）、Docker容器，以及通过WebAssembly实现的浏览器端版本（Datasette Lite）。  

**使用方法：**  
- 安装：通过Homebrew（`brew install datasette`）、pip（`pip install datasette`）或Docker。  
- 启动：运行`datasette serve 数据库路径`，默认访问地址为`http://localhost:8001`。  
- 部署：使用`datasette publish heroku/cloudrun 数据库文件`发布到云端。