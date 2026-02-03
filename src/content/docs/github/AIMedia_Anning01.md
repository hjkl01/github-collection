
---
title: AIMedia
---

### [Anning01 AIMedia](https://github.com/Anning01/AIMedia)  ![GitHub Repo stars](https://img.shields.io/github/stars/Anning01/AIMedia?style=social)

**项目核心内容总结：**

AIMedia 是一个全自动AI媒体管理软件，集成热点抓取、AI内容生成、多平台发布等功能，采用 Django 后端 + PySide6 桌面端架构，支持抖音、微博、搜狐等平台的新闻抓取，通过智谱AI和 Stable Diffusion 实现图文生成，并支持今日头条、微信公众号等平台的内容发布。项目包含企业级功能（如微信支付、登录），但需用户自行部署后端服务、打包前端应用并配置数据库及第三方接口。

**使用方法：**  
1. 克隆代码并创建虚拟环境（推荐 Conda）；  
2. 安装依赖（`pip install -r requirements.txt`）；  
3. 下载 Chrome 浏览器并放置至指定路径；  
4. 分别参考 `back/` 和 `pyside/` 目录下的文档启动后端和前端。

**主要特性：**  
- 全流程自动化：热点抓取 → AI创作 → 多平台发布；  
- 技术栈：Django 5.x + PySide6 + SQLite/PostgreSQL/MySQL；  
- 支持平台：抖音、微博、微信公众号等；  
- 新版本计划：迁移至 FastAPI + 浏览器插件架构（AiMaster 项目）。  

**部署要求：**  
需具备 Django 部署经验，自行配置数据库、微信接口，且需打包 PySide6 应用。项目定位为工程级，不适合开箱即用。