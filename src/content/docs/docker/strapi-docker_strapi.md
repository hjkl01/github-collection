
---
title: strapi-docker
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/strapi/strapi-docker?style=social) ](https://github.com/strapi/strapi-docker)
### [strapi strapi-docker](https://github.com/strapi/strapi-docker)

**核心内容总结：**

该项目提供 Strapi v3 的 Docker 镜像，用于容器化部署。主要功能包括：

1. **镜像类型**  
   - `strapi/strapi`：用于创建新项目或运行主机上的 Strapi 项目，支持通过环境变量配置数据库（SQLite/PostgreSQL/MySQL/MongoDB）等参数。  
   - `strapi/base`：用于构建自定义 Docker 镜像，适配生产环境部署。

2. **使用方法**  
   - **新建项目**：通过 `docker run` 命令挂载本地目录，镜像会自动执行 `strapi new` 创建项目（默认使用 SQLite）。  
   - **运行已有项目**：挂载本地项目目录，镜像会安装依赖并启动 `strapi develop`。  
   - **环境变量**：支持通过 `-e` 参数配置数据库连接信息（如 `DATABASE_HOST`、`DATABASE_USERNAME` 等）。

3. **注意事项**  
   - 镜像仅兼容 Strapi v3，v4 需使用社区工具（如 [strapi-tool-dockerize](https://github.com/strapi-community/strapi-tool-dockerize)）。  
   - 升级 Strapi 时需手动重建应用，因镜像标签更新不自动升级版本。  
   - 生产部署建议使用 `strapi/base` 构建自定义镜像，并参考示例中的 `Dockerfile`。  

4. **构建镜像**  
   通过 `yarn install` 和 `./bin/build.js` 命令可本地构建镜像。