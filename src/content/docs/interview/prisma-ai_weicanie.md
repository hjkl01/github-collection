
---
title: prisma-ai
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/weicanie/prisma-ai?style=social) ](https://github.com/weicanie/prisma-ai)
### [weicanie prisma-ai](https://github.com/weicanie/prisma-ai)

**项目核心内容总结：**

**功能**  
PrismaAI 是一款求职辅助 AI 工具，提供以下核心功能：  
1. **简历优化**：分析项目经历，挖掘亮点并生成可落地的简历内容，支持 AI Agent 协助实现项目功能。  
2. **岗位匹配**：实时抓取岗位信息，通过本地向量模型精准匹配适合的岗位，自动定制简历。  
3. **面试准备**：集成题库、思维导图与 Anki，支持高效记忆；提供结构化面经数据库，支持版本管理和共建。  

**使用方法**  
- **在线使用**：访问 [www.ai.pinkprisma.com](https://www.pinkprisma.com) 直接使用（部分功能需本地部署）。  
- **本地部署**：  
  1. 通过 Docker 部署：克隆仓库后执行 `./scripts/start.sh`。  
  2. 本地开发：安装依赖并配置 MySQL、Redis、MongoDB、MinIO 等服务，运行 `pnpm run dev`。  

**主要特性**  
- **AI 核心架构**：基于 Planer-Executor + CRAG + Human-in-the-loop，支持多轮反馈优化输出。  
- **技术栈**：前端使用 React + Vite，后端基于 Nest.js，AI 部分集成 LangChain、LangGraph 等。  
- **便捷部署**：提供 Docker 一键启动，支持 DeepWiki 集成作为项目知识库。  

**其他**  
- 支持简历 PDF 编辑与导出（v4.1.7）、AI 助手 Prisma（v5.0.0）等更新。  
- 项目遵循 AGPL-3.0 协议，部分组件使用自定义许可证。