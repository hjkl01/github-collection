
---
title: LibreTV
---

### [LibreSpark LibreTV](https://github.com/LibreSpark/LibreTV)

LibreTV 是一个轻量级、无需注册的在线视频搜索与播放平台，聚合多个视频源内容，支持多设备访问。项目提供多种部署方式（如 Vercel、Netlify、Cloudflare Pages、Docker 等），需设置 `PASSWORD` 环境变量以启用密码保护，禁止商业用途。  

**核心功能**：  
- 支持搜索与播放第三方 API 提供的视频内容  
- 提供标准苹果 CMS V10 API 兼容接口  
- 内置键盘快捷键（如空格播放/暂停、方向键调节进度等）  

**部署方式**：  
1. **云平台一键部署**：通过 Vercel、Netlify、Render 等平台的按钮直接创建实例。  
2. **自定义部署**：使用 Docker 或本地开发环境（需 Node.js 支持），配置 `.env` 文件并设置 `PASSWORD`。  

**注意事项**：  
- 项目不存储视频内容，仅作为搜索工具，用户需自行承担版权风险。  
- 部署时必须设置密码，否则将提示用户配置。  
- 推荐启用 GitHub Actions 自动同步主仓库更新，避免 Pull Bot 干扰。  

**技术特点**：  
- 前端采用 HTML5、Tailwind CSS、DPlayer 播放器  
- 后端集成 HLS 代理与 Serverless Functions  
- 支持本地存储与跨平台兼容性