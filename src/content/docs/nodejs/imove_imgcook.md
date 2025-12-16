
---
title: imove
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/imgcook/imove?style=social) ](https://github.com/imgcook/imove)
### [imgcook imove](https://github.com/imgcook/imove)

**iMove 核心内容总结：**

**项目功能**  
iMove 是一个面向前端开发者的逻辑编排工具，通过可视化流程图实现复杂逻辑的复用。由两部分组成：用于绘制流程的画布和用于执行流程的 imove-sdk。用户可在本地运行画布，编写代码并编排节点，导出流程描述语言（DSL），再通过 SDK 调用执行。

**使用方法**  
1. 克隆仓库并启动本地服务：`git clone` 后进入示例目录执行 `npm install` 和 `npm start`，浏览器访问 `http://localhost:8000`。  
2. 在画布中拖拽节点构建流程图。  
3. 配置节点名称和代码逻辑。

**主要特性**  
- **流程可视化**：通过图形化界面直观表达逻辑，降低理解门槛。  
- **逻辑复用**：支持节点复用及参数配置，提升开发效率。  
- **灵活扩展**：通过编写函数即可扩展节点，支持插件集成。  
- **适用场景广泛**：兼容前端（如点击事件、Ajax）和后端（如 Node.js）场景。  
- **多语言编译支持**：计划支持 JavaScript、Java 等语言编译（当前未实现）。  

**项目状态**  
标注为“INACTIVE”，可能处于非活跃开发状态。