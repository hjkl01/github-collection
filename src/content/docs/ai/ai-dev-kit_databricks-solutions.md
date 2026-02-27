
---
title: ai-dev-kit
---

### [databricks-solutions ai-dev-kit](https://github.com/databricks-solutions/ai-dev-kit)  ![GitHub Repo stars](https://img.shields.io/github/stars/databricks-solutions/ai-dev-kit?style=social)

**项目名称：Databricks AI 开发工具包**

---

### **核心内容总结**

**项目功能：**  
Databricks AI 开发工具包（AI Dev Kit）为 AI 编程助手（如 Claude Code、Cursor、Windsurf 等）提供可信的开发资源，加速在 Databricks 平台上构建各类应用。支持的功能包括：

- Spark 声明式管道（流表、CDC、SCD 类型 2、Auto Loader）
- Databricks 工作流（定时任务、多任务 DAG）
- AI/BI 仪表盘（可视化、KPI、分析）
- Unity Catalog（表、卷、治理）
- Genie Spaces（自然语言数据探索）
- 知识助手（基于 RAG 的文档问答）
- MLflow 实验（评估、评分、追踪）
- 模型服务（部署 ML 模型和 AI 代理到端点）
- Databricks 应用（全栈 Web 应用）

---

**使用方法：**

1. **安装到现有项目：**  
   提供了适用于 Mac/Linux 和 Windows 的安装脚本，支持全局或项目级安装，并可选择安装特定工具（如 Cursor）。

2. **可视化构建器应用：**  
   提供基于 Web 的全栈应用，集成聊天 UI，用于 Databricks 开发。

3. **核心库使用：**  
   可在 Python 项目中直接使用 `databricks_tools_core` 提供的高级 Databricks 函数，例如执行 SQL 查询。

---

**主要特性：**

- **模块化组件：**
  - `databricks-tools-core`：Python 库，包含高级 Databricks 函数。
  - `databricks-mcp-server`：MCP 服务器，提供 50+ 工具供 AI 助手使用。
  - `databricks-skills`：19 个 Markdown 技能文档，介绍 Databricks 最佳实践。
  - `databricks-builder-app`：集成 Claude Code 的 Web 应用，用于构建 Databricks 项目。

- **支持 AI 工具集成：**  
  可与 Claude Code、Cursor 等 AI 编程助手配合使用，提升开发效率。

- **多平台支持：**  
  提供 Linux、Mac 和 Windows 的安装脚本，便于不同环境部署。

- **灵活部署选项：**  
  支持项目级、全局安装，以及指定配置文件和工具的安装方式。

---

**许可证：**  
项目受 Databricks 许可协议约束，部分依赖库使用 MIT、AGPL、LGPL、Apache 等开源许可证。