
---
title: dootask
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/kuaifan/dootask?style=social) ](https://github.com/kuaifan/dootask)
### [kuaifan dootask](https://github.com/kuaifan/dootask)

**DooTask** 是一款开源的任务管理系统，支持多平台部署（CentOS/Debian/Ubuntu/macOS 等），提供任务管理、应用商店、SSL 配置等功能。  

**核心功能与使用方法：**  
1. **部署安装**：需 Docker 20.10+ 和 Docker Compose 2.0+，通过命令 `./cmd install` 一键安装，支持自定义端口。  
2. **基础操作**：支持密码重置（`./cmd repassword`）、端口修改（`./cmd port`）、服务启停（`./cmd up/down`）。  
3. **开发与构建**：需 Node.js 20+，开发模式使用 `./cmd dev`，生产构建使用 `./cmd prod`。  
4. **SSL 配置**：支持自动配置（`./cmd https`）或 Nginx 代理配置。  
5. **升级与迁移**：通过 `./cmd update` 升级，提供数据库备份与恢复（`./cmd mysql backup/recovery`）迁移功能。  
6. **卸载**：使用 `./cmd uninstall` 卸载项目。  

**主要特性：**  
- 基于 Docker 容器化部署，支持跨平台（Linux/Unix）。  
- 提供应用商店、多语言支持（含中文文档）。  
- 支持 HTTPS 自动配置与 Nginx 代理。  
- 提供详细的迁移与数据备份恢复流程。  
- 推荐硬件配置：2 核以上 CPU、4GB 内存。