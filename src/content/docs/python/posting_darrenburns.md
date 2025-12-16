
---
title: posting
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/darrenburns/posting?style=social) ](https://github.com/darrenburns/posting)
### [darrenburns posting](https://github.com/darrenburns/posting)

**核心内容总结：**

**项目功能**  
Posting 是一款终端 HTTP 客户端，支持类似 Postman 的请求管理功能，通过 YAML 文件存储请求，支持版本控制。可导入导出 curl 命令、Postman 集合及 OpenAPI 接口，支持运行 Python 代码扩展功能。

**使用方法**  
通过终端命令 `posting` 启动，支持 Vim 快捷键和自定义键位。安装方式包括：  
1. 使用 `uv` 工具安装（推荐）：  
   ```bash  
   curl -LsSf https://astral.sh/uv/install.sh | sh  
   uv tool install --python 3.13 posting  
   ```  
2. 使用 `pipx` 安装：  
   ```bash  
   pipx install posting  
   ```  

**主要特性**  
- 键盘操作优先，支持 SSH 环境使用  
- 支持环境变量、自动补全、语法高亮  
- 可自定义主题、快捷键及配置  
- 支持在编辑器中打开请求文件  
- 提供命令面板快速访问功能  
- 支持 Python 代码预处理/后处理请求