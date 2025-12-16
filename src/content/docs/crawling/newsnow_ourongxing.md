
---
title: newsnow
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/ourongxing/newsnow?style=social) ](https://github.com/ourongxing/newsnow)
### [ourongxing newsnow](https://github.com/ourongxing/newsnow)

**项目核心内容总结：**

**功能特点**  
- 提供简洁优雅的界面，支持实时更新热门新闻；  
- 支持GitHub账号登录及数据同步；  
- 默认30分钟缓存（登录用户可强制刷新），根据新闻源更新频率自动调整抓取间隔，优化资源使用并避免IP封禁；  
- 支持自定义MCP服务器（提供配置示例）；  
- 未来计划增加多语言、个性化分类及全球新闻源。  

**部署方式**  
1. **基础部署**：Fork仓库后导入Cloudflare Page或Vercel；  
2. **Cloudflare Page**：构建命令`pnpm run build`，输出目录`dist/output/public`；  
3. **Docker**：项目根目录执行`docker compose up`；  
4. **数据库**：推荐使用Cloudflare D1，需配置`wrangler.toml`文件。  

**关键配置**  
- GitHub OAuth需创建App并设置回调地址`https://your-domain.com/api/oauth/github`，填写Client ID/Secret及JWT密钥；  
- 环境变量参考`.env.server`文件，首次运行需启用`INIT_TABLE=true`；  
- MCP服务器可修改`BASE_URL`为自定义域名。  

**开发要求**  
- 依赖Node.js 20+，使用`pnpm`安装依赖并启动开发环境；  
- 新增数据源需参考`shared/sources`和`server/sources`目录的类型定义及架构。