
---
title: create-react-app
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/facebook/create-react-app?style=social) ](https://github.com/facebook/create-react-app)
### [facebook create-react-app](https://github.com/facebook/create-react-app)

### 核心内容总结

**项目功能**  
Create React App 是一个用于快速创建 React 应用的工具，无需手动配置构建工具（如 Webpack、Babel），提供开箱即用的开发环境和生产构建流程。

**使用方法**  
1. 通过 `npx create-react-app my-app`、`npm init react-app my-app` 或 `yarn create react-app my-app` 创建项目。  
2. 进入项目目录并运行 `npm start` 或 `yarn start` 启动开发服务器，访问 `http://localhost:3000` 查看应用。  
3. 使用 `npm test` 运行测试，`npm build` 构建生产版本。

**主要特性**  
- **无需配置**：自动集成 React、TypeScript、ES6 等功能，隐藏底层构建工具。  
- **开箱即用**：包含测试框架（Jest）、开发服务器、代码格式化（ESLint）和 PWA 支持。  
- **灵活扩展**：可通过 `eject` 暴露底层配置，自定义构建流程。  
- **跨平台支持**：适用于单页应用（SPA）开发，但不支持服务端渲染（需使用 Next.js 等工具）。  

**注意事项**  
项目已弃用，不推荐用于新项目，建议迁移至其他现代 React 框架（如 Vite、Next.js）。