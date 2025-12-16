
---
title: claude-code-templates
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/davila7/claude-code-templates?style=social) ](https://github.com/davila7/claude-code-templates)
### [davila7 claude-code-templates](https://github.com/davila7/claude-code-templates)

**项目核心内容总结：**  
该项目提供Anthropic Claude Code的预配置模板，包含AI代理、自定义命令、外部服务集成（MCPs）、设置、自动化钩子和项目模板，用于提升开发效率。  

**功能与特性：**  
- **组件类型**：涵盖代码审查、安全审计、性能优化等AI代理；测试生成、代码优化等自定义命令；GitHub、PostgreSQL等MCPs集成；超时设置、内存配置等参数调整；Git提交前验证等自动化钩子。  
- **附加工具**：实时开发监控、远程对话查看、系统健康检查、插件管理界面。  
- **安装方式**：支持通过`npx`命令直接安装指定组件（如`--agent`、`--command`），或交互式浏览安装。  

**使用方法：**  
1. 安装完整开发栈：`npx claude-code-templates@latest --agent development-team/frontend-developer ...`  
2. 交互式安装：`npx claude-code-templates@latest`  
3. 安装单个组件：`npx claude-code-templates@latest --agent development-tools/code-reviewer --yes`  

**其他信息：**  
- 提供在线模板浏览平台（[aitmpl.com](https://aitmpl.com)）和文档（[docs.aitmpl.com](https://docs.aitmpl.com)）。  
- 项目基于MIT许可证，支持社区贡献，包含来自开源项目的组件（如`wshobson/agents`、`awesome-claude-code`）。