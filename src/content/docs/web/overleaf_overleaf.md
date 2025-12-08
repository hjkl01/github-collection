
---
title: overleaf
---

### [overleaf overleaf](https://github.com/overleaf/overleaf)

**项目核心内容总结：**

**功能**  
Overleaf 是一个开源的在线实时协作 LaTeX 编辑器，提供社区版（开源）和企业版（付费）两种版本。社区版支持本地部署，适用于信任用户环境；企业版提供增强的安全性（如 LDAP/SAML 单点登录）、管理功能和协作特性（如版本追踪）。

**使用方法**  
- **安装**：通过 [Overleaf Toolkit](https://github.com/overleaf/toolkit/) 获取详细安装指南。  
- **构建 Docker 镜像**：使用 `make build-base` 和 `make build-community` 命令构建基础镜像和社区版镜像。  
- **升级**：参考 GitHub Wiki 的 [版本更新说明](https://github.com/overleaf/overleaf/wiki#release-notes) 进行升级。  

**主要特性**  
- 实时协作编辑与 LaTeX 编译支持。  
- 社区版基于 Docker 镜像（`sharelatex/sharelatex`），依赖 `texlive` 等基础依赖。  
- 企业版提供更高级的安全、管理及协作功能。  
- 开源协议：采用 GNU AFFERO GENERAL PUBLIC LICENSE 3.0。  

**注意事项**  
社区版不适用于需要用户隔离的场景（如无沙箱编译时，用户可访问容器资源）。企业版需联系官方获取支持。