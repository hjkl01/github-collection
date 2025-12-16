
---
title: free-font
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/jaywcjlove/free-font?style=social) ](https://github.com/jaywcjlove/free-font)
### [jaywcjlove free-font](https://github.com/jaywcjlove/free-font)

### 项目核心内容总结

**项目功能**  
1. 收集并提供**商用免费中文字体**（含艺术体、黑体、宋体等分类），支持用户下载和使用。  
2. 提供**字体预览海报生成**功能，辅助用户查看字体效果。  
3. 支持**Docker镜像部署**，快速搭建本地预览服务。  

**使用方法**  
1. **本地开发**：  
   - 安装依赖（`npm install`）。  
   - 通过 `npm run one` 生成单个字体预览海报，或 `npm run all` 生成所有字体海报及HTML页面。  
   - 使用 `npm run dev` 或 `npm run start` 生成网站。  
2. **部署**：  
   - 通过 Docker 镜像（`wcjiang/free-font`）快速部署服务。  

**主要特性**  
- 支持多种授权协议（如商免、OFL-1.1、IPA-1.0）。  
- 字体分类管理（如英文字体单独归类）。  
- **大文件限制**：单个字体文件不超过50MB（GitHub存储限制）。  
- **镜像网站**：提供多个镜像站点（如 haoziku.com、Vercel 等）供访问。  

**注意事项**  
- 项目不承担字体版权风险，用户需自行确认授权范围。  
- 由于费用问题，已取消预览页面功能，但不影响字体下载使用。