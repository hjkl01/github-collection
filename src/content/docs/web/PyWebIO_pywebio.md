
---
title: PyWebIO
---

### [pywebio PyWebIO](https://github.com/pywebio/PyWebIO)

PyWebIO 是一个 Python 库，允许用户通过脚本方式快速构建交互式 Web 应用或浏览器 GUI 应用，无需掌握 HTML 和 JavaScript。其核心功能包括：  
- **同步交互**：通过函数直接获取用户输入并输出结果，类似终端操作；  
- **非声明式布局**：简化界面设计，降低开发复杂度；  
- **框架兼容性**：支持与 Flask、Django、Tornado 等主流 Web 框架集成；  
- **异步支持**：兼容 `asyncio` 和协程；  
- **可视化扩展**：可结合 Plotly、Bokeh 等库实现数据可视化。  

**使用方法**：  
1. 安装：`pip3 install -U pywebio`；  
2. 编写脚本：通过 `input` 和 `output` 函数实现用户交互（如 BMI 计算示例）；  
3. 部署为 Web 服务：使用 `start_server` 启动应用；  
4. 集成到 Web 框架：通过对应框架的 Handler 实现接口嵌入。