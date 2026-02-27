
---
title: Agent-Skills-for-Context-Engineering
---

### [muratcankoylan Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)  ![GitHub Repo stars](https://img.shields.io/github/stars/muratcankoylan/Agent-Skills-for-Context-Engineering?style=social)

**项目核心内容总结：**

该项目是一个开源的“Agent 技能库”，专注于“上下文工程（Context Engineering）”，用于构建生产级的 AI Agent 系统。其核心目标是通过科学地管理语言模型的上下文窗口，提升 Agent 的性能和效果。

---

### **项目功能：**

- **上下文工程原理**：不同于传统的 Prompt 工程，上下文工程关注的是如何优化模型所接收的所有信息（包括系统提示、工具定义、文档、历史对话、工具输出等），以应对模型注意力机制的限制。
- **技能分类**：技能分为五大类，涵盖基础、架构、操作、开发方法和认知架构。
- **平台无关性**：技能适用于多种平台（如 Claude Code、Cursor 等），不依赖特定供应商。
- **示例与模板**：提供完整的系统设计示例，展示技能的实际应用，如数字大脑系统、LLM 作为评判者的工具、书籍微调流水线等。

---

### **主要特性：**

- **渐进式披露**：技能内容按需加载，提升效率。
- **平台无关设计**：技能适用于多种 Agent 平台，便于移植。
- **概念+实践结合**：每个技能提供理论基础和 Python 伪代码示例，便于理解和实现。
- **技能触发机制**：根据任务关键词自动激活相关技能。
- **插件化安装**：支持通过命令行或界面安装特定插件。
- **可扩展性**：鼓励社区贡献，遵循开源开发模式。

---

### **使用方法：**

1. **通过 Claude Code 安装插件**：
   - 添加插件源：`/plugin marketplace add muratcankoylan/Agent-Skills-for-Context-Engineering`
   - 安装插件，如：`/plugin install context-engineering-fundamentals@context-engineering-marketplace`

2. **用于 Cursor 或 IDE**：
   - 将技能内容复制到 `.rules` 文件或项目技能文件夹中。

3. **自定义实现**：
   - 提取技能中的原理和模式，应用到自己的 Agent 框架中。

---

### **技能分类概览：**

| 类别 | 示例技能 |
|------|----------|
| 基础技能 | 上下文基础、退化模式、压缩策略 |
| 架构技能 | 多 Agent 模式、记忆系统、工具设计 |
| 运维技能 | 上下文优化、评估、高级评估 |
| 开发方法 | 项目开发流程 |
| 认知架构 | BDI 心理状态建模 |

---

### **示例项目：**

- **数字大脑系统**：展示模块化设计、自动化脚本、记忆管理。
- **X 到书系统**：多 Agent 系统，监控社交媒体并生成书籍。
- **LLM 作为评判者工具**：实现评分、对比、偏见缓解。
- **书籍微调流水线**：训练模型模仿特定作者风格。

---

### **授权与贡献：**

- 使用 MIT 协议，鼓励社区贡献。
- 贡献需遵循模板结构，保持简洁、可执行、有示例。