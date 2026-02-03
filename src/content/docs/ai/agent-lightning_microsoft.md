
---
title: agent-lightning
---

### [microsoft agent-lightning](https://github.com/microsoft/agent-lightning)  ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/agent-lightning?style=social)

**项目核心内容总结：**  
Agent Lightning 是一个用于训练 AI 代理的框架，支持无需代码更改即可优化任意代理（如 LangChain、AutoGen 等），并可选择性优化多代理系统中的部分代理。主要特性包括：  
1. **零代码更改优化**：通过轻量级工具（如 `agl.emit_xxx()`）实现代理优化。  
2. **兼容性**：支持主流代理框架（如 LangChain、CrewAI）及无框架的 OpenAI 使用场景。  
3. **算法支持**：集成强化学习、自动提示优化等算法，提升代理性能。  
4. **灵活架构**：通过追踪器收集数据，算法模块化处理，训练器整合资源与优化结果。  

**使用方法**：  
通过 `pip install agentlightning` 安装，参考文档和示例代码快速上手。