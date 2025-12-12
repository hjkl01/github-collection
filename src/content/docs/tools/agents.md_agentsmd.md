
---
title: agents.md
---

### [agentsmd agents.md](https://github.com/agentsmd/agents.md)

AGENTS.md 是一个为 AI 编码代理提供标准化指导的开放格式文件，用于明确项目协作规则和操作流程。其核心功能包括：

1. **开发环境配置**  
   提供命令示例（如使用 `pnpm dlx turbo run` 快速定位项目、通过 `pnpm create vite` 初始化项目等），帮助代理快速理解开发环境结构。

2. **测试规范**  
   定义测试流程：通过 `pnpm turbo run test` 执行多包测试、使用 `pnpm vitest run` 精准定位测试用例，并要求修复所有测试/类型错误。

3. **PR 规范**  
   规范提交格式（标题包含项目名）、强制要求提交前执行 `pnpm lint` 和 `pnpm test`。

4. **项目特性**  
   - 结构化文档：包含开发提示、测试指令、PR 规则三部分  
   - 可预测性：为代理提供统一的操作指引  
   - 可扩展性：支持通过 `.github/workflows` 自定义 CI 流程  

项目附带 Next.js 官网（https://agents.md/），可本地运行（需执行 `pnpm install` 和 `pnpm run dev`）。