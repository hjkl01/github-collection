
---
title: skopeo
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/containers/skopeo?style=social) ](https://github.com/containers/skopeo)
### [containers skopeo](https://github.com/containers/skopeo)

Skopeo 是一个用于管理容器镜像和仓库的命令行工具，支持跨存储机制操作，无需依赖守护进程或 root 权限。核心功能包括：  
1. **镜像操作**：复制镜像（支持 Docker、OCI、本地目录等存储类型）、检查镜像信息（如标签、摘要、配置）、删除镜像、同步仓库与本地目录。  
2. **认证管理**：通过 `login/logout` 命令管理私有仓库凭证，或直接通过 `--creds` 参数指定用户名和密码。  
3. **特性**：兼容 Docker 和 OCI 标准，支持多种传输协议（如 HTTPS），可处理镜像签名（生成/验证 sigstore 密钥对）。  

**使用示例**：  
- 查看镜像信息：`skopeo inspect docker://myregistrydomain.com:5000/busybox`  
- 复制镜像：`skopeo copy --src-creds=testuser:testpassword docker://myregistrydomain.com:5000/private oci:local_oci_image`  
- 同步仓库：`skopeo sync --src docker --dest dir registry.example.com/busybox /media/usb`