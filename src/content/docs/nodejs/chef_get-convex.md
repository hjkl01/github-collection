
---
title: chef
---

### [get-convex chef](https://github.com/get-convex/chef)

**项目核心内容总结：**  
Chef 是一个基于 Convex 开源数据库构建的 AI 应用开发工具，支持零配置认证、文件上传、实时 UI 和后台工作流，可生成全栈 Web 应用。其核心功能依赖于 Convex 的 API，适合代码生成场景。  

**使用方法：**  
1. **在线使用**：通过 [Chef 官网](https://chef.convex.dev) 直接使用，提供免费试用。  
2. **本地运行**：  
   - 克隆项目并安装依赖（需 `nvm` 和 `pnpm`）。  
   - 配置 `.env.local` 环境变量，设置 Convex OAuth 客户端信息及模型提供商 API 密钥（如 OpenAI、Anthropic 等）。  
   - 运行 `pnpm run dev` 启动前端，`npx convex dev` 启动 Convex 后端。  

**主要特性：**  
- 基于 Convex 数据库，支持实时同步与后台任务。  
- 提供 OAuth 授权集成，需自行替换生产环境认证系统。  
- 包含代码生成模板、CLI 工具（chefshot）和测试框架（test-kitchen）。  

**注意事项：**  
- 本地运行使用 Convex 控制平面，但不计入用户账户资源消耗。  
- 生产环境需自定义 OAuth 流程，推荐使用 OAuth 2.0 授权码模式。