### [CopilotKit CopilotKit](https://github.com/CopilotKit/CopilotKit)  ![GitHub Repo stars](https://img.shields.io/github/stars/CopilotKit/CopilotKit?style=social)

CopilotKit 是一个用于构建全栈代理原生应用、生成式 UI 和聊天应用程序的 SDK。其核心功能包括：

1. **聊天 UI**：基于 React 的界面，支持消息流式传输、工具调用及代理响应。
2. **生成式 UI**：允许代理根据用户意图和状态，在运行时动态生成和更新 UI 组件。
3. **共享状态**：提供同步状态层，实现代理与 UI 组件间的实时读写。
4. **人机协作流程**：支持代理在执行中暂停，以请求用户输入、确认或修改。
5. **后端工具渲染**：代理可调用后端工具，并将其返回的 UI 组件直接渲染在客户端。

该项目采用 AG-UI 协议连接 UI、代理和工具，支持与 LangGraph、CrewAI 等集成，并通过 `useAgent` 钩子提供对代理的编程控制。