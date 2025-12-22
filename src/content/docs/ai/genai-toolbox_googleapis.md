
---
title: genai-toolbox
---

### [googleapis genai-toolbox](https://github.com/googleapis/genai-toolbox)  ![GitHub Repo stars](https://img.shields.io/github/stars/googleapis/genai-toolbox?style=social)

**项目核心内容总结：**

**项目功能：**  
Toolbox 是一个用于构建基于 Gemini 的 AI 代理的工具包，支持与数据库、数据仓库等数据源交互。提供定义数据源、工具、提示（prompt）等功能，并兼容多种编程语言（如 Python、JavaScript、Go）及 Gemini CLI 扩展。

**使用方法：**  
1. 通过 `tools.yaml` 配置文件定义数据源（如 PostgreSQL）、工具（如 SQL 查询）及工具集（工具分组）。  
2. 使用 SDK（如 Python、JavaScript、Go）加载工具集，实现与数据源的交互。  
3. 支持通过 Gemini CLI 扩展直接调用预定义或自定义工具，以自然语言操作数据源。

**主要特性：**  
- 支持多种数据源（PostgreSQL、BigQuery、Cloud SQL 等）和工具类型（SQL 查询、数据分析等）。  
- 提供工具集管理功能，支持按需加载不同工具分组。  
- 集成 Gemini CLI 扩展，实现命令行直接调用工具。  
- 支持 `tools.yaml` 配置文件定义资源、工具、提示模板等。  
- 版本控制遵循语义化版本（SemVer），明确 API 变更规则。