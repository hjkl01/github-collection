
---
title: json-render
---

### [vercel-labs json-render](https://github.com/vercel-labs/json-render)  ![GitHub Repo stars](https://img.shields.io/github/stars/vercel-labs/json-render?style=social)

**json-render 项目核心内容总结：**

**项目功能**  
通过 AI 生成可预测的 UI 组件（如仪表板、数据可视化等），但输出内容严格受限于用户预定义的组件目录，确保安全性与一致性。

**使用方法**  
1. **定义组件目录**：使用 TypeScript 定义允许 AI 使用的组件（如 Card、Metric）及对应属性和动作（如导出报告、刷新数据）。  
2. **注册组件**：通过 React 实现组件渲染逻辑，将 JSON 结构映射为实际 UI 元素。  
3. **AI 生成**：用户输入自然语言提示（如“生成营收仪表板”），AI 根据目录生成 JSON 结构，前端实时渲染。

**主要特性**  
- **受约束输出**：AI 仅能使用预定义组件，避免生成不可控内容。  
- **条件显示**：支持基于数据、权限或逻辑的组件可见性控制（如错误提示仅在特定条件下显示）。  
- **交互动作**：支持带确认对话框的按钮操作（如退款），并可绑定数据路径和回调处理。  
- **验证机制**：内置表单验证规则（如必填、邮箱格式校验），提升数据准确性。  
- **流式渲染**：AI 生成 JSON 时，前端逐步渲染，提升交互响应速度。

**许可证**  
Apache-2.0 开源协议。