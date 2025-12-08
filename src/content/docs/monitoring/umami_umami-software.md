
---
title: umami
---

### [umami-software umami](https://github.com/umami-software/umami)

**项目功能**：Umami 是一个简单、快速且注重隐私的 Google Analytics 替代方案，提供网站访问数据分析功能。  

**使用方法**：  
1. **从源码安装**：需 Node.js 18.18+ 和 PostgreSQL 12.14+，通过 `git clone` 获取代码后配置 `.env` 文件，执行 `pnpm install`、`pnpm build` 和 `pnpm start` 启动。  
2. **Docker 安装**：使用 `docker pull` 获取镜像，通过 `docker compose up -d` 部署（包含 PostgreSQL 数据库）。  

**主要特性**：  
- 开源（MIT 许可证）；  
- 自动创建管理员账号（用户名 admin，密码 umami）；  
- 提供在线演示环境；  
- 支持通过 GitHub、Twitter、LinkedIn、Discord 等渠道获取支持。