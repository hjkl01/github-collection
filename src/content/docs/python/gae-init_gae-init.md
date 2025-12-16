
---
title: gae-init
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/gae-init/gae-init?style=social) ](https://github.com/gae-init/gae-init)
### [gae-init gae-init](https://github.com/gae-init/gae-init)

**项目核心内容总结：**

**项目功能**  
gae-init 是一个基于 Python、Flask 和 Google App Engine 的项目模板，集成 RESTful API、Bootstrap 前端框架及多种开发工具，用于快速构建和部署 Web 应用。

**使用方法**  
1. **初始化**：进入项目目录后运行 `yarn` 安装依赖，全局安装 `gulp-cli`。  
2. **开发环境**：执行 `gulp` 启动本地服务器，访问 `http://localhost:3000`。  
3. **部署**：使用 `gulp deploy` 命令部署到 Google App Engine，支持指定项目名和版本。  
4. **重置**：运行 `gulp reset` 重置项目并重新安装依赖。  

**主要特性**  
- 技术栈：Python 2.7、Flask、NDB、Jinja2、Bootstrap、jQuery、Less 等。  
- 工具支持：集成 Gulp、Bower，支持自动化构建和测试。  
- 测试功能：提供本地测试脚本，验证页面响应及应用启动能力。  
- 部署灵活：支持多项目部署、版本控制及禁用自动推广。  

**适用平台**：支持 macOS、Linux 和 Windows 系统。