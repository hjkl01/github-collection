
---
title: Claudable
---

### [opactorai Claudable](https://github.com/opactorai/Claudable)

**核心内容总结：**  
Claudable 是一个基于 Next.js 的 Web 应用构建工具，结合 Claude Code 等 AI 代理的代码生成能力与直观的 UI 设计，用户可通过自然语言描述需求（如“创建一个带暗黑模式的任务管理应用”），自动生成代码并实时预览。支持部署到 Vercel、集成 Supabase 数据库，无需复杂配置。  

**主要功能：**  
- 自然语言转代码，生成生产级 Next.js 项目  
- 实时预览与热重载  
- 零配置启动，无需 API 密钥或数据库设置  
- 支持多种 AI 编码代理（Claude Code、Cursor CLI、Qwen Code 等）  
- 集成 GitHub、Vercel 和 Supabase  

**使用方法：**  
1. 安装 Node.js 18+、Git 及支持的 AI 代理（如 Claude Code）  
2. 克隆仓库并安装依赖：`git clone https://github.com/opactorai/Claudable.git && cd Claudable && npm install`  
3. 启动开发服务器：`npm run dev`，访问 http://localhost:3000  

**技术栈：**  
- 数据库：Supabase（PostgreSQL）  
- 部署：Vercel 一键发布  
- UI 框架：Tailwind CSS、shadcn/ui  

**其他：**  
- 提供桌面应用（Electron）构建命令  
- 支持数据库备份、重置等操作  
- 开源 MIT 协议，免费使用