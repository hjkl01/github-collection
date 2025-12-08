
---
title: simpleui
---

### [newpanjing simpleui](https://github.com/newpanjing/simpleui)

**项目功能**  
SimpleUI 是 Django Admin 的一个主题，基于 Element-UI 和 Vue 重构，提供更友好、现代化的界面。支持 28 种主题，兼容原生 Django Admin，无需修改代码即可安装使用。  

**主要特性**  
- 配置简单：在 `settings.py` 中添加 `simpleui` 即可生效；  
- 兼容性强：支持 Django 5.3、Python 3.12；  
- 界面优化：采用 Element-UI 设计风格，提升交互体验；  
- 功能扩展：提供专业版（Simple Pro），支持自定义组件、拖拽式首页设计等。  

**使用方法**  
1. 安装：`pip install django-simpleui`；  
2. 配置：在 `INSTALLED_APPS` 首行添加 `'simpleui'`；  
3. 启动项目后自动生效。  

**其他**  
支持 Docker 快速部署，提供中文和英文文档，常见问题包括静态文件收集（`collectstatic`）及国际化配置。