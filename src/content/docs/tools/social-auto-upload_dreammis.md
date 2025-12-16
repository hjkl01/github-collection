
---
title: social-auto-upload
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/dreammis/social-auto-upload?style=social) ](https://github.com/dreammis/social-auto-upload)
### [dreammis social-auto-upload](https://github.com/dreammis/social-auto-upload)

**项目核心内容总结**：

**功能**：  
`social-auto-upload` 是一个自动化工具，支持将视频一键上传至抖音、B站、小红书、快手、视频号、百家号、TikTok 等平台，提供定时上传、多平台扩展、API 封装、Docker 部署等功能。当前支持国内主流平台，国外平台逐步扩展（如 YouTube 计划中）。

**使用方法**：  
1. **安装**：克隆项目、安装依赖（需 Python 3.10+）、安装 Playwright 浏览器驱动。  
2. **配置**：修改 `conf.py` 设置 Chrome 路径，创建 `cookiesFile` 和 `videoFile` 文件夹，初始化数据库。  
3. **准备素材**：生成平台 Cookie（通过示例脚本），将视频文件（及封面、描述文本）放入 `videos` 目录。  
4. **执行上传**：运行示例脚本（如 `upload_video_to_douyin.py`）实现上传。  
5. **Docker 部署**：支持自定义构建镜像或使用预构建镜像运行。

**主要特性**：  
- 模块化设计，支持平台扩展（如新增 uploader 模块）。  
- 提供 CLI 和 Web 管理界面（Vue 版本）。  
- 支持定时任务、多线程优化（开发中）。  
- 文档完善（[官方文档链接](https://sap-doc.nasdaddy.com/)），社区支持（微信公众号、交流群）。  
- 开源 MIT 许可证，接受贡献（GitHub PR）。  

**注意事项**：  
- 部分功能（如 Cookie 管理、Proxy 设置）尚未完善。  
- 项目由开发者维护，建议技术用户参与修复问题或提交功能增强。