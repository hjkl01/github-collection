
---
title: next-ai-draw-io
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/DayuanJiang/next-ai-draw-io?style=social) ](https://github.com/DayuanJiang/next-ai-draw-io)
### [DayuanJiang next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io)

**项目核心内容总结**：

**功能**：  
Next AI Draw.io 是一款结合 AI 的图表创建工具，支持通过自然语言生成/修改 draw.io 图表，提供多云架构（AWS/GCP/Azure）图标支持、动画连接器、图表版本历史管理及实时交互式聊天界面。

**使用方法**：  
1. **在线体验**：无需安装，直接访问演示站点（需注意 API 限制）。  
2. **Docker 部署**：通过环境变量配置 AI 提供商（如 OpenAI、Anthropic 等）和 API 密钥运行容器。  
3. **本地安装**：克隆代码、安装依赖、配置 `.env.local` 文件后启动开发服务器。

**主要特性**：  
- 支持多 AI 提供商（OpenAI、Anthropic、Google、Azure 等）及自定义模型（如 Claude Sonnet 4.5、GPT-5.1）。  
- 可上传图像/图表并由 AI 自动复制优化。  
- 支持云架构图（AWS/GCP/Azure）生成及动态连接器。  
- 提供图表版本历史回溯功能。  
- 技术栈基于 Next.js、Vercel AI SDK 和 react-drawio。  

**注意事项**：  
- 部署需设置 `ACCESS_CODE_LIST` 防止资源滥用。  
- 离线部署需配置 `embed.diagrams.net` 替代方案。