### [stagehand](https://github.com/browserbase/stagehand) ![GitHub Repo stars](https://img.shields.io/github/stars/browserbase/stagehand?style=social)

Stagehand 是一个 AI 浏览器自动化框架，支持将**自然语言指令**与**编程代码**结合来控制网页操作，兼顾灵活性与可维护性。  
核心功能包括：用 `act()` 执行单步操作、用 `agent()` 处理多步骤任务、用 `extract()` 按结构化 schema 提取页面数据。  
它强调生产可用性：支持在“AI 驱动”与“可复用代码流程”之间切换，可预览 AI 动作，并通过自动缓存与自愈机制在页面变化时自动恢复，减少对 LLM 推理的依赖、提升稳定性与成本效率。  
项目提供完整文档、快速初始化（`npx create-browser-app`）和从源码构建方式，采用 MIT 许可证。