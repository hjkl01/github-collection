
---
title: SaveAny-Bot
---

### [krau SaveAny-Bot](https://github.com/krau/SaveAny-Bot)  ![GitHub Repo stars](https://img.shields.io/github/stars/krau/SaveAny-Bot?style=social)

**项目核心内容总结**  

**功能**：  
Save Any Bot 是一款 Telegram 文件保存工具，支持保存文档、视频、图片、贴纸等文件，甚至可绕过“限制保存内容”的媒体限制。支持批量下载、流式传输、多用户管理、自动按规则整理文件，并可通过监控指定聊天自动保存消息（支持过滤）。用户可通过编写 JS 插件解析并保存几乎所有网站的文件。  

**存储后端**：  
支持本地文件系统、Alist、S3、WebDAV、Telegram（重新上传至指定聊天）等存储方式。  

**使用方法**：  
1. 创建 `config.toml` 配置文件，设置 Telegram 机器人 Token、存储路径等参数。  
2. 通过 Docker 命令运行容器，挂载配置文件和下载目录。  
3. 详细配置可参考项目文档。  

**主要特性**：  
- 绕过 Telegram 限制保存内容的媒体；  
- 支持多用户、自动整理文件；  
- 可监控聊天并自动保存消息；  
- 自定义 JS 插件解析网站文件；  
- 多种存储后端灵活适配。