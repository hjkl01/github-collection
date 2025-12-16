
---
title: jellyfin-web
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/jellyfin/jellyfin-web?style=social) ](https://github.com/jellyfin/jellyfin-web)
### [jellyfin jellyfin-web](https://github.com/jellyfin/jellyfin-web)

**项目核心内容总结：**  
Jellyfin Web 是 Jellyfin 项目的核心前端，用于桌面浏览器、Android 和 iOS 客户端。项目支持社区贡献，翻译可通过 Weblate 实现。  

**使用方法：**  
1. 安装 Node.js 及 npm；  
2. 克隆仓库并运行 `npm install` 安装依赖；  
3. 通过 `npm start` 启动开发环境；  
4. 使用 `npm run build:development` 构建客户端。  

**主要特性：**  
- 模块化架构，支持多应用（如管理面板、实验性功能等）；  
- 支持多语言翻译及动态加载插件；  
- 目录结构基于 Bulletproof React 规范，部分模块需清理或重构（如 `controllers`、`elements` 等）。