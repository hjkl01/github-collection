### [imgcook imove](https://github.com/imgcook/imove)  ![GitHub Repo stars](https://img.shields.io/github/stars/imgcook/imove?style=social)

iMove 是一个面向 JavaScript 开发者的逻辑编排工具库（目前状态为非活跃），旨在解决复杂逻辑复用问题。

**核心组成与流程**
1. **流程画布**：本地 HTTP 服务运行，支持可视化拖拽节点、编写代码及配置参数，最终导出 DSL 文件。
2. **运行时 SDK**：将导出的流程集成至项目中，通过 SDK 调用执行。

**主要特性**
* **流程可视化**：绘图方便，逻辑表达直观，易于理解。
* **逻辑复用**：节点支持复用，单节点支持灵活参数配置。
* **灵活可扩展**：仅需编写函数即可扩展节点，支持插件集成。
* **全场景适用**：适用于前端点击事件、组件生命周期、Ajax 请求、Node.js 后端 API 等所有 JavaScript 场景。

**技术基础**
基于 AntV X6 绘图引擎开发，包含画布服务与运行时 SDK 两部分。