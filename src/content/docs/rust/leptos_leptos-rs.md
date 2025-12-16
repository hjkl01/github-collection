
---
title: leptos
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/leptos-rs/leptos?style=social) ](https://github.com/leptos-rs/leptos)
### [leptos-rs leptos](https://github.com/leptos-rs/leptos)

**项目功能**  
Leptos 是一个基于 Rust 的全栈 Web 框架，使用细粒度响应式系统构建声明式用户界面。支持客户端和服务器端渲染，提供服务器函数集成、HTML 流式传输等特性，适用于构建高性能 Web 应用。

**使用方法**  
通过 `cargo-leptos` 安装框架，使用类似 JSX 的模板语法编写组件，结合响应式信号（signals）和派生状态（derived values）实现数据驱动的 UI 更新。示例代码展示如何定义组件并绑定交互逻辑。

**主要特性**  
1. **细粒度响应式**：组件首次渲染后，仅更新依赖状态的 DOM 节点，避免全量重渲染，性能优于基于虚拟 DOM（VDOM）的框架（如 Yew）。  
2. **全栈支持**：支持服务端渲染（SSR）、客户端渲染（CSR）及混合模式，集成服务器函数（Server Functions）实现前后端数据交互。  
3. **流式传输**：通过 `<Suspense>` 支持 HTML 流式传输，提升首屏加载速度。  
4. **生态兼容**：与 Dioxus、Sycamore 等框架对比，更注重 Web 性能优化（如 WASM 二进制体积更小），同时支持桌面端应用开发。  
5. **开发体验**：提供声明式模板语法，结合 `Copy + 'static` 信号设计，提升代码可读性和开发效率。  

**适用场景**  
适合需要高性能、全栈集成及响应式交互的 Web 项目，尤其适合需要服务端渲染或流式传输的复杂应用。