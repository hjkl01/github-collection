
---
title: crontab-ui
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/alseambusher/crontab-ui?style=social) ](https://github.com/alseambusher/crontab-ui)
### [alseambusher crontab-ui](https://github.com/alseambusher/crontab-ui)

**核心内容总结：**

**项目功能**  
Crontab UI 是一个用于图形化管理 Linux 系统定时任务（crontab）的工具，通过 Web 界面实现任务的添加、删除、暂停、恢复、备份、导出和导入，避免手动编辑 crontab 文件时可能引发的错误。

**主要特性**  
- 支持从现有 crontab 文件导入任务  
- 提供任务备份与恢复功能  
- 支持多机器间任务导出与导入  
- 每个任务独立的日志记录  
- 支持 HTTP 基本认证、SSL 加密、自定义存储路径  
- 可通过环境变量配置主机地址、端口、基础路径等参数  
- 自动保存任务到系统 crontab  

**使用方法**  
1. **本地安装**  
   - 安装 Node.js 后，通过 `npm install -g crontab-ui` 全局安装，运行 `crontab-ui` 启动服务  
   - 通过环境变量（如 `HOST`、`PORT`、`CRON_DB_PATH` 等）自定义配置  

2. **Docker 部署**  
   - 使用预构建镜像：`docker run -d -p 8000:8000 alseambusher/crontab-ui`  
   - 支持挂载本地目录存储数据（如日志、数据库）  
   - 可通过环境变量设置认证信息（`BASIC_AUTH_USER`、`BASIC_AUTH_PWD`）  

3. **其他功能**  
   - 支持通过 `--autosave` 参数自动同步任务到系统 crontab  
   - 提供邮件通知和钩子（hooks）扩展功能  

**注意事项**  
- 需确保 Node.js 权限正确（如 `npm` 安装路径权限）  
- 导入任务前建议先备份原有 crontab 数据