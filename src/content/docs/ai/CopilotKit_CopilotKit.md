
---
title: CopilotKit
---

### [CopilotKit CopilotKit](https://github.com/CopilotKit/CopilotKit)  ![GitHub Repo stars](https://img.shields.io/github/stars/CopilotKit/CopilotKit?style=social)

CopilotKit 是构建全栈代理应用、生成式 UI 及聊天应用的 SDK。核心功能包括：
1. **Chat UI**：基于 React 的聊天界面，支持消息流式传输、工具调用和代理响应。
2. **生成式 UI**：代理可根据用户意图动态生成及更新运行时 UI 组件。
3. **后端工具渲染**：支持代理调用后端工具返回的 UI 组件直接渲染。
4. **共享状态**：代理与 UI 组件间提供实时同步读写状态的分层机制。
5. **人在回路**：支持代理在执行流程中暂停，以请求用户输入、确认或编辑。

项目采用 AG-UI 协议连接代理工作流与用户端应用，提供 `useAgent` 钩子控制代理连接，支持 LangGraph、CrewAI 等集成。