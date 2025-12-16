
---
title: mergestat
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/mergestat/mergestat?style=social) ](https://github.com/mergestat/mergestat)
### [mergestat mergestat](https://github.com/mergestat/mergestat)

**项目核心内容总结：**

MergeStat 是一个允许通过 SQL 查询 Git 仓库数据的工具，支持从 GitHub API 等来源获取数据，用于分析代码历史和内容。  

**使用方法：**  
1. 通过 `docker-compose up` 启动本地实例。  
2. 访问 `http://localhost:3300/` 进入管理界面，添加仓库并同步数据。  
3. 若需使用 GitHub API（如自动导入仓库），需配置 GitHub 个人访问令牌（PAT）。  

**主要特性：**  
- 提供图形化管理界面，支持 PAT 管理。  
- 支持本地 Git 仓库和 GitHub API 数据源。  
- 可通过 SQL 查询代码历史、仓库内容等信息。  
- 提供示例和文档（[文档链接](https://docs.mergestat.com/)）。