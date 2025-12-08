
---
title: imove
---

### [ykfe imove](https://github.com/ykfe/imove)

iMove 是一个面向前端开发者的逻辑编排工具，用于解决复杂逻辑复用问题。项目由两部分组成：**画布**（用于流程设计）和 **imove-sdk**（用于执行流程）。通过本地启动 HTTP 服务运行画布，用户可拖拽节点绘制流程图，配置节点逻辑并导出 DSL，最终在项目中通过 imove-sdk 调用执行。

**主要特性**：  
- 流程可视化：通过图形化界面直观表达逻辑；  
- 逻辑复用：支持节点复用和参数配置；  
- 灵活扩展：通过编写函数即可扩展节点功能；  
- 适用场景广泛：支持前端事件、Ajax 请求、Node.js 后端 API 等；  
- 多语言编译（待实现）：未来将支持 Java 等语言的代码生成。

**使用方法**：  
1. 克隆仓库并启动示例：  
   ```bash  
   git clone https://github.com/ykfe/imove.git  
   cd imove/example  
   npm install && npm start  
   ```  
2. 在浏览器访问 `http://localhost:8000`，通过画布拖拽节点、配置逻辑并导出 DSL。