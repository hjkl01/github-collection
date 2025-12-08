
---
title: analytics
---

### [plausible analytics](https://github.com/plausible/analytics)

**Plausible Analytics 核心内容总结：**  

**项目功能**  
Plausible Analytics 是一款开源、隐私友好的网站分析工具，替代 Google Analytics。支持数据统计、用户行为追踪、自定义事件、团队协作、数据导出等功能，符合 GDPR/CCPA 等隐私法规。  

**使用方法**  
1. **云托管服务**：通过官方订阅服务快速部署，无需管理服务器，数据仅在欧盟处理。  
2. **自托管（Plausible CE）**：开源版本需自行部署服务器，功能略有简化（如无高级分析功能）。  

**主要特性**  
- **隐私保护**：不使用 Cookie，不存储用户 IP 或个人数据。  
- **轻量高效**：脚本体积小，加载速度快，支持 SPA 和哈希路由。  
- **数据管理**：提供邮件/Slack 报告、CSV 导出、API 接口及 Looker Studio 连接。  
- **团队协作**：支持成员邀请、权限分配、公开数据链接。  
- **合规性**：数据仅在欧盟处理，符合 Schrems II 规定。  
- **技术栈**：基于 Elixir/Phoenix、PostgreSQL 和 ClickHouse 构建，前端使用 TailwindCSS 和 React。  

**适用场景**  
适合注重隐私、需自托管或希望减少依赖广告技术的网站所有者。