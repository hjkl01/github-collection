
---
title: tabby
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/TabbyML/tabby?style=social) ](https://github.com/TabbyML/tabby)
### [TabbyML tabby](https://github.com/TabbyML/tabby)

Tabby 是一款开源的自托管AI编程助手，提供类似GitHub Copilot的本地部署方案。其核心功能包括：无需依赖数据库或云服务、支持消费级GPU、提供OpenAPI接口便于集成到现有开发环境。主要特性包含代码补全、文档知识库整合、多模型支持（如Codestral、CodeGemma等）、团队协作功能（如Answer Engine知识引擎）以及企业级管理功能（如LDAP认证、存储统计等）。

使用方法可通过Docker一键启动，示例命令为：`docker run -it --gpus all -p 8080:8080 -v $HOME/.tabby:/data tabbyml/tabby serve --model StarCoder-1B --device cuda`。项目提供详细文档指导安装、配置及IDE插件集成（支持VSCode、IntelliJ等）。贡献者可通过Git克隆代码库并使用Rust环境构建项目。