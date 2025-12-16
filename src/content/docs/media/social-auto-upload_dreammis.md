
---
title: social-auto-upload
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/dreammis/social-auto-upload?style=social) ](https://github.com/dreammis/social-auto-upload)
### [dreammis social-auto-upload](https://github.com/dreammis/social-auto-upload)

### 项目核心内容总结

**项目功能**  
`social-auto-upload` 是一个自动化工具，支持将视频一键上传至抖音、B站、小红书、快手、视频号、百家号及 TikTok 等平台，提供定时上传、多平台配置扩展等功能。  

**主要特性**  
- 支持国内主流平台（抖音、B站、小红书等）及国外平台（TikTok）；  
- 提供定时上传、Cookie 管理（部分实现）、Proxy 设置（部分实现）；  
- 支持 GUI/CLI 交互优化、API 封装、Docker 部署；  
- 计划扩展 YouTube 平台及增加自动化调度、多线程上传等功能。  

**使用方法**  
1. **安装**：克隆项目，安装 Python 依赖及 Playwright 浏览器驱动；  
2. **配置**：修改 `conf.py` 文件，设置本地浏览器路径、Cookie 存储路径等；  
3. **准备内容**：生成各平台 Cookie 文件，准备视频及封面文件；  
4. **运行**：启动后端（`sau_backend.py`）和前端（`npm run dev`），通过示例脚本（如 `upload_video_to_douyin.py`）执行上传。  

**其他说明**  
- 项目由社区维护，鼓励开发者提交 PR 修复问题或新增功能；  
- 提供 Docker 镜像，支持一键部署；  
- 采用 MIT 开源许可证。