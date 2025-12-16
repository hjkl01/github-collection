
---
title: once-campfire
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/basecamp/once-campfire?style=social) ](https://github.com/basecamp/once-campfire)
### [basecamp once-campfire](https://github.com/basecamp/once-campfire)

**项目核心内容总结：**

**功能特性：**  
Campfire 是一款支持多房间聊天、私信、文件预览、搜索、网络推送通知、@提及、API 接口及机器人集成的 Web 聊天应用。所有房间可设置访问权限，支持单租户部署（公共房间对所有用户开放）。

**使用方法：**  
- **Docker 部署**：  
  1. 构建镜像（`docker build -t campfire .`）；  
  2. 运行容器时映射 `/rails/storage` 卷用于数据持久化；  
  3. 通过环境变量配置 SSL 域名（`SSL_DOMAIN`）、VAPID 密钥（用于推送通知）、Sentry 错误监控等；  
  4. 示例命令：`docker run` 搭配端口映射、卷挂载及环境变量参数。  
- **开发环境**：运行 `bin/setup` 初始化，再执行 `bin/rails server` 启动服务。

**注意事项：**  
首次启动需创建管理员账户，其邮箱将显示在登录页供密码重置联系。单租户架构下，若需隔离不同客户群，需部署多个实例。