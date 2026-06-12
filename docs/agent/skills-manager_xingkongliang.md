### [skills-manager](https://github.com/xingkongliang/skills-manager) ![GitHub Repo stars](https://img.shields.io/github/stars/xingkongliang/skills-manager?style=social)

Skills Manager 是一款用于统一管理 AI 编码工具技能（skills）的桌面应用，核心功能包括：

- 提供统一技能库：支持从 Git 仓库、本地文件夹、`.zip/.skill` 压缩包及 skills.sh 市场安装技能，集中存储并可自定义路径。  
- 集成市场与 AI 搜索：可浏览热门技能、关键词搜索，并支持通过 API Key 启用 SkillsMP AI 搜索。  
- 多工具一键同步：可通过软链接或复制方式，将技能同步到多种已支持的 AI 工具。  
- 场景（Scenarios）管理：可将技能按场景分组，配置每个场景的代理开关、排序，并在侧边栏快速切换全局技能方案。  
- 项目工作区（Project Workspaces）：管理项目内本地技能目录，支持与中心库双向同步、批量启停、差异对比、嵌套目录与按代理导出。  
- 链接工作区（Linked Workspaces）：可将任意目录作为技能根目录独立管理。  
- 批量操作与筛选：支持多选技能进行启用/禁用、导出、删除，并可通过标签和来源快速过滤大型技能库。  
- 更新与预览：可检查 Git 来源技能更新、重导入本地技能，查看 `SKILL.md/README.md`、源元数据及上下游内容对比。  
- 自定义工具支持：可新增自定义代理/工具，或覆盖内置工具默认技能路径。  
- Git 备份恢复：支持将技能库纳入 Git 版本管理，实现多机同步、版本快照与历史恢复。  
- 完整设置中心：可统一配置仓库路径、同步模式、默认场景、主题、语言、代理、托盘行为、Git 远程和更新检查等。  

支持工具包括 Cursor、Claude Code、Codex、OpenCode、Amp、Kilo Code、Roo Code、Goose、Gemini CLI、GitHub Copilot、Windsurf、TRAE IDE、Antigravity、Clawdbot、Droid，并支持扩展自定义工具。