
---
title: open-webui
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/open-webui/open-webui?style=social) ](https://github.com/open-webui/open-webui)
### [open-webui open-webui](https://github.com/open-webui/open-webui)

**核心内容总结：**

**项目功能**  
Open WebUI 是一个基于 Web 的用户界面，支持与 Ollama（本地模型服务）或 OpenAI API（云端模型服务）进行交互，提供本地化部署和模型管理功能。

**使用方法**  
1. **Docker 安装**：  
   - 默认配置（本地 Ollama）：`docker run` 命令启动容器，映射端口 3000。  
   - 连接远程 Ollama：通过 `-e OLLAMA_BASE_URL` 设置远程服务器地址。  
   - GPU 加速：使用 `--gpus all` 参数并指定 `:cuda` 标签的镜像。  
   - 自带 Ollama：使用 `:ollama` 标签的镜像，集成 Ollama 服务。  
2. **其他方式**：支持 Docker Compose、Kustomize、Helm 等安装方法，或参考文档进行原生安装。  

**主要特性**  
- **多模型支持**：兼容 Ollama 本地模型和 OpenAI API 云端模型。  
- **硬件加速**：支持 Nvidia GPU 加速（需 CUDA 环境）。  
- **数据持久化**：通过 Docker 卷 `-v open-webui:/app/backend/data` 保存数据库和配置。  
- **离线模式**：设置 `HF_HUB_OFFLINE=1` 防止联网下载模型。  
- **自动更新**：使用 Watchtower 工具自动更新 Docker 容器。  
- **开发分支**：提供 `:dev` 标签的不稳定版本，包含最新功能但可能有缺陷。  

**注意事项**  
- 连接远程 Ollama 时需正确配置网络参数（如 `--network=host`）。  
- 安装前需确保 Docker 环境已配置，GPU 使用需安装 Nvidia 工具包。