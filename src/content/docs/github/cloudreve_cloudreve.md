
---
title: cloudreve
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/cloudreve/cloudreve?style=social) ](https://github.com/cloudreve/cloudreve)
### [cloudreve cloudreve](https://github.com/cloudreve/cloudreve)

Cloudreve 是一款自托管的多云文件管理系统，支持将文件存储到本地、远程节点、OneDrive、S3 兼容 API、七牛云、阿里云 OSS 等多种存储服务。核心功能包括：  
- **文件传输**：支持客户端直连上传/下载，集成 Aria2/qBittorrent 实现后台多节点下载。  
- **文件管理**：批量下载、压缩/解压/预览归档文件，提取媒体元数据并按标签搜索。  
- **协作与分享**：多用户分组管理，生成带过期时间的分享链接，在线预览视频、图片、文档等。  
- **扩展性**：支持 WebDAV 协议，拖拽上传，自定义主题颜色、暗黑模式及 PWA 应用。  

**使用方法**：  
- 通过 [快速入门](https://docs.cloudreve.org/overview/quickstart) 指南本地部署测试，或参考 [部署文档](https://docs.cloudreve.org/overview/deploy/) 部署到生产环境。  
- 从源码构建可参考 [构建指南](https://docs.cloudreve.org/overview/build/)。  

**技术栈**：后端基于 Go + Gin + ent，前端使用 React + Redux + Material-UI。  
**授权协议**：GPL V3。