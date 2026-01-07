
---
title: memos
---

### [usememos memos](https://github.com/usememos/memos)  ![GitHub Repo stars](https://img.shields.io/github/stars/usememos/memos?style=social)

Memos 是一款开源的自托管笔记工具，采用 Go 和 React 开发，支持 Markdown 编辑与存储，强调隐私保护和数据自主性。用户可完全掌控数据，无需依赖云服务，且无广告、无订阅费用。核心功能包括：  
- **隐私安全**：本地部署、无数据追踪  
- **快速性能**：基于 Go 后端和 React 前端优化加载速度  
- **灵活部署**：支持 Docker 一键安装、Docker Compose、Kubernetes 等多种方式  
- **开发友好**：提供 REST 和 gRPC 接口，支持集成到现有工作流  
- **界面简洁**：支持暗色模式和移动端适配  

使用方法推荐通过 Docker 部署，执行命令 `docker run -d -p 5230:5230 -v ~/.memos:/var/opt/memos neosmemo/memos:stable` 后访问 `http://localhost:5230` 即可使用。项目采用 MIT 开源协议，提供中文及多语言文档支持。