### [vercel-labs json-render](https://github.com/vercel-labs/json-render)  ![GitHub Repo stars](https://img.shields.io/github/stars/vercel-labs/json-render?style=social)

json-render 是一个生成式 UI 框架，旨在让 AI 根据自然语言提示安全地生成动态、个性化的用户界面，其输出受限于用户预定义的组件目录和 Schema。

主要特性：
- **安全可控**：AI 只能使用定义好的组件和操作，确保输出 JSON 始终符合预期 Schema。
- **跨平台渲染**：同一套规范可渲染为 React/Vue（Web）、React Native（移动端）、Remotion（视频）、React PDF（文档）、React Email（邮件）及图片。
- **流式处理**：支持流式接收 AI 响应并渐进式渲染 UI。
- **高级交互**：支持动态属性绑定、条件可见性、状态监听及 Action 触发（如 setState）。
- **开箱即用**：内置 36 个 shadcn/ui 组件，支持 Redux、Zustand 等多种状态管理库适配器。

工作流程：定义组件目录与 Schema -> 实现组件逻辑 -> 传入 AI 生成的 JSON 规范进行渲染。