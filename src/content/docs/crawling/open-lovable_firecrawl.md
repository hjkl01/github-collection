
---
title: open-lovable
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/firecrawl/open-lovable?style=social) ](https://github.com/firecrawl/open-lovable)
### [firecrawl open-lovable](https://github.com/firecrawl/open-lovable)

**项目功能**：通过AI聊天快速生成React应用，由Firecrawl团队开发，提供本地开发示例及云解决方案Lovable.dev。  

**使用方法**：  
1. 克隆仓库并安装依赖；  
2. 配置.env.local文件，填写Firecrawl及至少一个AI服务商（Gemini/Anthropic/OpenAI/Groq）的API密钥，可选配置Morph API；  
3. 选择沙盒环境（默认Vercel，需配置Vercel OIDC Token或Personal Access Token；或使用E2B需填写E2B API密钥）；  
4. 运行`pnpm dev`启动本地开发服务器。  

**主要特性**：支持多AI服务商集成，提供Vercel或E2B沙盒选项，MIT开源许可。