
---
title: aios-core
---

### [SynkraAI aios-core](https://github.com/SynkraAI/aios-core)  ![GitHub Repo stars](https://img.shields.io/github/stars/SynkraAI/aios-core?style=social)

### 项目核心内容总结

#### 项目名称  
Synkra AIOS - 通用智能代理框架  

#### 项目功能  
Synkra AIOS 是一个基于智能代理的自动化开发框架，支持全栈开发、敏捷开发、创意写作、商业战略、个人健康、教育等多个领域。其核心功能包括：  
- **智能代理协作**：多个智能代理（如分析师、产品经理、架构师、开发人员、测试人员等）协同工作，完成从需求分析到代码实现的全过程。  
- **自主开发引擎（ADE）**：支持从用户需求到可执行代码的自动转换，包括需求分析、计划制定、执行、质量审查和自动恢复等七个阶段。  
- **多语言支持**：提供英语、葡萄牙语、西班牙语、中文等多语言文档。  
- **IDE 集成**：支持多种开发工具（如 Claude Code、Gemini CLI、Codex CLI、Cursor、GitHub Copilot、AntiGravity）的集成和配置。  
- **模块化扩展**：支持创建和使用“Squads”（智能代理团队），可扩展至任意领域。  
- **版本控制与协作**：提供 Git 工作流、分支保护、代码审查等支持团队协作的功能。  

#### 使用方法  
1. **安装**  
   - 新项目：`npx aios-core init meu-projeto`  
   - 现有项目：`cd seu-projeto && npx aios-core install`  
   - 更新：`npx aios-core@latest install`  

2. **配置 IDE**  
   - 根据使用的 IDE（如 Cursor、Claude Code、Codex CLI 等）配置对应的规则文件（如 `.cursor/global-rules.md`、`.claude/CLAUDE.md`、`AGENTS.md` 等）。  

3. **启动智能代理**  
   - 激活特定代理（如 `@dev`、`@qa` 等），并执行初始命令（如 `*help`）验证系统是否正常运行。  

4. **开发流程**  
   - 使用代理进行需求分析、架构设计、任务拆解、代码实现和质量审查。  
   - 支持通过 Web 界面和命令行界面（CLI）进行操作。  

5. **Squads 扩展**  
   - 创建或使用已有的 Squads，扩展 AIOS 的功能到其他领域（如商业战略、教育、健康等）。  

#### 主要特性  
1. **CLI 优先架构**：所有核心功能通过命令行实现，界面和监控为辅助功能。  
2. **自主开发引擎（ADE）**：将需求转化为代码的完整流程，包含工作树管理、迁移、规格管道、执行引擎、恢复系统、质量审查和记忆层等七个阶段。  
3. **智能代理协作**：多个代理（如 `@analyst`、`@pm`、`@architect`、`@dev`、`@qa` 等）分工协作，提高开发效率和质量。  
4. **多 IDE 支持**：兼容多种开发环境，提供相应的配置和同步命令。  
5. **文档丰富**：提供多语言文档、用户指南、技术架构、故障排除、安全最佳实践等。  
6. **团队协作功能**：支持 Git 工作流、分支保护、代码审查、CI/CD 等团队协作功能。  
7. **扩展性强**：支持创建自定义 Squads，扩展到任意领域。  

#### 项目结构  
- `docs/`：多语言文档和用户指南  
- `squads/`：Squads 扩展模块  
- `.aios-core/`：AIOS 核心配置和脚本  
- `scripts/`：脚本工具（如分支保护设置）  
- `CHANGELOG.md`：版本更新日志  
- `LICENSE`：MIT 开源许可证  

#### 适用场景  
- 软件开发（全栈开发、测试、部署）  
- 商业战略规划与执行  
- 创意写作与内容创作  
- 教育与知识管理  
- 个人健康与自我提升  

#### 项目现状  
- 开源（MIT 许可）  
- 支持贡献（欢迎提交 PR）  
- 提供 Pro 版（高级功能，仅限 AIOS 高级成员）  
- 活跃开发与维护（GitHub Actions、CI/CD、分支保护等）  

---