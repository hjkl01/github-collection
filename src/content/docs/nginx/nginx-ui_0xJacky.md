
---
title: nginx-ui
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/0xJacky/nginx-ui?style=social) ](https://github.com/0xJacky/nginx-ui)
### [0xJacky nginx-ui](https://github.com/0xJacky/nginx-ui)

**项目核心内容总结：**

**功能**  
Nginx UI 是一个图形化管理工具，支持创建/管理 Nginx 站点配置、SSL 证书配置、自动备份及恢复配置文件、通过 Docker 容器部署等。

**使用方法**  
1. **直接运行**：下载可执行文件后，通过命令行启动（支持后台运行）。  
2. **Systemd 服务**：通过安装脚本自动注册为服务，使用 `systemctl` 控制启停。  
3. **Docker 部署**：提供 Docker 镜像，通过挂载配置目录和端口映射实现快速部署。  

**主要特性**  
- 支持 Linux、macOS、Windows 等多平台（包括 ARM 架构）。  
- 自动适配 Debian 系统的 Nginx 配置规范（`sites-available/sites-enabled` 结构）。  
- 提供 Web 界面完成初始配置，支持 HTTPS 证书自动申请。  
- 集成 Docker，可替代宿主机 Nginx，支持容器内静态文件托管。  
- 开源协议为 GNU Affero GPL v3.0。