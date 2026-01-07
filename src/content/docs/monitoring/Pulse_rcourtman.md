
---
title: Pulse
---

### [rcourtman Pulse](https://github.com/rcourtman/Pulse)  ![GitHub Repo stars](https://img.shields.io/github/stars/rcourtman/Pulse?style=social)

**项目核心内容总结**  
Pulse 是一款用于监控 Proxmox、Docker 和 Kubernetes 基础设施的实时统一仪表板，提供集中化的指标、警报和 AI 分析功能。  

**主要功能**  
- **统一监控**：支持 Proxmox、Docker、Kubernetes 等多平台，自动发现设备，查看系统状态和备份信息。  
- **智能告警**：支持 Discord、Slack、Telegram 等多渠道通知，支持 AI 分析告警原因。  
- **AI 功能**：内置聊天助手、定时健康检查（Patrol）、成本跟踪等 AI 工具。  
- **安全与便捷**：数据加密、OIDC/SSO 认证、一键更新，无数据上传。  

**使用方法**  
- **Proxmox LXC 安装**：执行一键脚本快速部署。  
- **Docker 安装**：通过 Docker 命令启动容器，访问 `http://<IP>:7655`。  

**特色**  
- 提供免费版与付费版（Pulse Pro），后者增加自动化巡检（AI Patrol）、根因分析等高级功能。  
- 支持 Home Assistant 插件等社区扩展。  
- 开源 MIT 许可，支持赞助开发。