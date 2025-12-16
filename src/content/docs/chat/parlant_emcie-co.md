
---
title: parlant
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/emcie-co/parlant?style=social) ](https://github.com/emcie-co/parlant)
### [emcie-co parlant](https://github.com/emcie-co/parlant)

**项目核心内容总结：**

Parlant 是一个 AI 代理开发框架，旨在解决传统 LLM 代理难以遵循指令、行为不可预测等问题。其核心功能是通过**规则定义**和**行为指南**确保代理严格遵循预设逻辑，而非依赖 LLM 自主理解提示词。

**主要特性：**
- **规则驱动**：用自然语言定义行为规则（如“用户询问退款时先检查订单状态”），框架自动匹配并执行。
- **结构化控制**：支持定义对话流程（Journeys）、领域术语（Glossary）、预设回复模板（Canned Responses）等。
- **工具集成**：可绑定外部 API、数据库等工具，实现自动化操作。
- **可解释性**：追踪每条规则的匹配与执行过程，提升透明度。
- **企业级功能**：包含风险控制、对话分析、React 聊天组件等。

**使用方法：**
1. 安装：`pip install parlant`
2. 编写代码定义工具函数、变量及行为规则（如示例中的天气查询代理）。
3. 启动服务，通过本地地址访问测试界面。

**适用场景**：金融、医疗、电商、法律等需严格合规的领域，支持规模化部署与持续优化。