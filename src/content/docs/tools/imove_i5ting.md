
---
title: imove
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/i5ting/imove?style=social) ](https://github.com/i5ting/imove)
### [i5ting imove](https://github.com/i5ting/imove)

**项目核心内容总结：**  

iMove 是一个面向前端开发者的逻辑编排工具，通过可视化流程图实现复杂逻辑的复用与管理。项目由两部分组成：**画布**（用于流程设计）和 **imove-sdk**（用于执行流程）。用户可通过本地 HTTP 服务运行画布，拖拽节点构建流程图，配置节点参数并导出 DSL 代码，再通过 SDK 集成到项目中执行。  

**主要特性：**  
- 流程可视化：直观绘制逻辑流程，降低理解成本；  
- 逻辑复用：支持节点复用与参数配置；  
- 灵活扩展：通过编写函数即可扩展节点功能；  
- 适用场景广泛：支持前端事件、Ajax 请求、Node.js 后端等场景；  
- 多语言编译（待实现）：未来支持 JavaScript、Java 等语言的代码生成。  

**使用方法：**  
1. 克隆仓库并启动示例项目：`git clone` → `npm install` → `npm start`，访问 `http://localhost:8000`；  
2. 在画布中拖拽节点构建流程图；  
3. 配置节点名称与代码逻辑，导出 DSL 并通过 imove-sdk 调用执行。  

**适用场景：**  
前端流程（如点击事件）、后端流程（如 Node.js）、前后端联动（如 Ajax 请求与后端 API 结合）。