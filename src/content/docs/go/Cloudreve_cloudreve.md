
---
title: Cloudreve
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/cloudreve/Cloudreve?style=social) ](https://github.com/cloudreve/Cloudreve)
### [cloudreve Cloudreve](https://github.com/cloudreve/Cloudreve)

### 项目核心内容总结

**Cloudreve** 是一个自托管的多云文件管理系统，支持将文件存储到本地、OneDrive、S3兼容API、七牛Kodo、阿里云OSS、腾讯云COS等主流云存储平台。  

**功能与特性**  
- 支持客户端直接上传/下载文件，集成Aria2/qBittorrent实现后台多节点下载。  
- 支持压缩/解压文件、批量下载、WebDAV协议、拖拽上传及断点续传。  
- 提取媒体元数据并支持按标签/元数据搜索文件，提供多用户分组管理及带过期时间的分享链接。  
- 在线预览视频、图片、音频、ePub文件，并支持编辑文本、图表、Markdown、Office文档。  
- 支持自定义主题颜色、深色模式、PWA应用及多语言。  

**使用方法**  
- 通过[快速开始指南](https://docs.cloudreve.org/overview/quickstart)进行本地测试部署，生产环境可参考[完整部署文档](https://docs.cloudreve.org/overview/deploy/)。  
- 提供Docker镜像（[Docker Hub](https://hub.docker.com/r/cloudreve/cloudreve)），支持一键部署。  
- 源码构建及贡献方式详见[构建文档](https://docs.cloudreve.org/overview/build/)和[贡献指南](https://docs.cloudreve.org/api/contributing/)。  

**技术栈**  
后端基于Go + Gin + ent，前端使用React + Redux + Material-UI。  

**授权协议**  
遵循GPL V3开源协议。