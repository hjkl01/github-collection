
---
title: vaultwarden
---

### [dani-garcia vaultwarden](https://github.com/dani-garcia/vaultwarden)

**项目核心内容总结：**  

**项目功能**  
Vaultwarden 是一个用 Rust 编写的 Bitwarden 客户端 API 替代服务器实现，兼容官方 Bitwarden 客户端，支持自托管部署。主要功能包括：  
- 个人保险库、发送功能、附件管理、网站图标  
- 组织功能（集合、密码共享、成员角色、目录同步等）  
- 多因素认证（Authenticator、Email、FIDO2、YubiKey、Duo）  
- 紧急访问、管理员后台、修改后的 Web Vault 客户端  

**使用方法**  
推荐通过容器镜像（支持 Docker、Podman、ghcr.io、quay.io 等）部署：  
1. **Docker 命令行**：拉取镜像并运行容器，需设置域名、挂载数据卷、开放端口。  
   ```shell
   docker run --detach --name vaultwarden --env DOMAIN="https://vw.domain.tld" --volume /vw-data/:/data/ --publish 127.0.0.1:8000:80 vaultwarden/server:latest
   ```  
2. **Docker Compose**：创建 `compose.yaml` 文件配置服务。  
   ```yaml
   services:
     vaultwarden:
       image: vaultwarden/server:latest
       environment:
         DOMAIN: "https://vw.domain.tld"
       volumes:
         - ./vw-data/:/data/
       ports:
         - 127.0.0.1:8000:80
   ```  
建议通过反向代理配置 HTTPS 以满足 Web Crypto API 安全要求。  

**主要特性**  
- 轻量高效，适合资源有限的自托管环境  
- 完整实现 Bitwarden 客户端 API 的大部分功能  
- 社区驱动，提供 Wiki 文档和多渠道支持（Matrix、GitHub 讨论、Discourse）  
- 开源 AGPL-3.0 协议，支持贡献者和第三方包扩展