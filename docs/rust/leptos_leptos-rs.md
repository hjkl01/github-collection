### [leptos-rs leptos](https://github.com/leptos-rs/leptos)  ![GitHub Repo stars](https://img.shields.io/github/stars/leptos-rs/leptos?style=social)

Leptos 是一个基于 Rust 的全栈、同构 Web 框架，用于构建声明式用户界面。其主要功能包括：

1. **全栈支持**：支持客户端渲染、服务器端渲染及混合模式（水合），支持数据与 HTML 的 HTTP 流式传输。
2. **细粒度响应式**：基于信号直接更新 DOM，无虚拟 DOM 开销，具有高性能和低代码量特点。
3. **同质服务器函数**：支持在组件中直接调用服务器端逻辑（如数据库请求），无需维护独立的 REST API。
4. **声明式 UI**：提供 `view!` 宏或构建器语法来定义用户界面。
5. **Web 标准兼容**：路由和交互设计遵循 Web 原生规范（如链接和表单）。
6. **构建工具**：推荐使用 `cargo-leptos` 配合 Actix 或 Axum 后端进行全栈开发。

框架 API 基本稳定，处于生产就绪状态，适用于需要高性能 Web 应用的场景。