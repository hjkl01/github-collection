
---
title: datasette
---

### [simonw datasette](https://github.com/simonw/datasette)  ![GitHub Repo stars](https://img.shields.io/github/stars/simonw/datasette?style=social)

Datasette 是一个用于探索和发布数据的开源工具，可将任意数据转换为交互式的可探索网站及 API。

主要功能包括：
1. 数据服务：通过命令行启动 Web 服务器，支持 SQLite 等数据的交互式浏览与 API 查询。
2. 元数据配置：支持 metadata.json 文件，用于定义网站标题、许可及来源信息。
3. 云端部署：支持一键打包 Docker 镜像，将数据发布至 Heroku 或 Google Cloud Run。
4. 浏览器运行：提供 Datasette Lite 版本，基于 WebAssembly 无需服务器即可在浏览器中直接运行。