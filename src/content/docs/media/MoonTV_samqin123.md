
---
title: MoonTV
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/samqin123/MoonTV?style=social) ](https://github.com/samqin123/MoonTV)
### [samqin123 MoonTV](https://github.com/samqin123/MoonTV)

**MoonTV核心内容总结：**  
1. **项目功能**：跨平台影视聚合播放器，支持多源影视搜索（如电影天堂等）、在线播放、收藏与播放记录同步、PWA离线访问、响应式布局适配不同设备，支持Android TV（需配合OrionTV）。  
2. **使用方法**：  
   - 部署方式：支持Docker（含Redis）、Vercel、Cloudflare等，需设置`USERNAME`/`PASSWORD`环境变量（非localstorage存储时）。  
   - 配置自定义：通过`config.json`调整资源站API、缓存时间、分类标签等，无需重新构建。  
   - 管理功能：管理员可通过`/admin`路径动态配置服务。  
3. **主要特性**：  
   - 多存储方式：支持localstorage、Redis、Upstash、Cloudflare D1。  
   - 安全性：强制密码保护，关闭公网注册，避免版权风险。  
   - 扩展性：支持自定义分类（如“华语电影”）、搜索关键词、接口替换。  
   - 已实现功能：深色模式、多账户、持久化存储。  
4. **注意事项**：  
   - 仅供个人使用，禁止公开分享或商业用途。  
   - 部署时需设置强密码，避免法律风险。  
   - Android TV端暂不支持与网页端数据同步。