
---
title: jira
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/teamatldocker/jira?style=social) ](https://github.com/teamatldocker/jira)
### [teamatldocker jira](https://github.com/teamatldocker/jira)

**项目核心内容总结：**

该项目是一个基于 Docker 的 Jira 容器镜像，支持快速部署和管理 Jira 应用。其主要功能包括：

- **支持多种数据库连接**，如 PostgreSQL，并提供连接配置方法。
- **支持自定义配置**，如 Tomcat 的 `server.xml`，允许用户进行更细粒度的配置。
- **支持 SSO 认证**，可通过环境变量启用 Atlassian Crowd 的单点登录功能。
- **支持扩展和自定义**，允许用户基于该镜像添加工具或修改启动脚本。
- **支持升级和回滚**，提供详细的升级流程和数据备份/恢复方法，确保升级过程安全可控。
- **提供调试模式**，便于开发和测试时使用。

**使用方法：**

- 使用 Docker 命令启动容器，通过环境变量配置数据库、SSO、自定义配置等。
- 支持通过挂载卷的方式将自定义配置文件（如 `server.xml`）引入容器。
- 提供完整的升级和回滚流程，包括数据备份、镜像更新、容器重启等步骤。

**主要特性：**

- 支持多种数据库连接。
- 提供 SSO 认证配置。
- 支持自定义配置和扩展。
- 提供详细的升级和回滚流程。
- 支持调试模式。