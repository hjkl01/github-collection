
---
title: skills
---

### [openai skills](https://github.com/openai/skills)  ![GitHub Repo stars](https://img.shields.io/github/stars/openai/skills?style=social)

**项目核心内容总结：**

Agent Skills 是一种用于 AI 代理的技能包，包含指令、脚本和资源，可帮助代理在特定任务中高效执行。技能可重复使用，支持在不同场景中调用。

该项目是为 Codex 提供的技能集合，支持技能的使用、分发和创建。用户可通过 Codex 提供的 `$skill-installer` 工具安装技能。

**使用方法：**
- 系统技能（`.system` 文件夹）会自动安装。
- 安装精选技能（`.curated`）只需指定名称，如：`$skill-installer gh-address-comments`。
- 安装实验性技能（`.experimental`）需指定文件夹或 GitHub URL。
- 安装后需重启 Codex 以生效。

**主要特性：**
- 技能模块化，便于复用。
- 支持自动安装和手动安装。
- 提供官方技能和自定义技能支持。
- 技能目录中包含 `LICENSE.txt` 文件，标明许可协议。

**参考资料：**
- 使用技能：[Codex 技能使用文档](https://developers.openai.com/codex/skills)
- 创建自定义技能：[创建技能文档](https://developers.openai.com/codex/skills/create-skill)
- 技能开放标准：[Agent Skills 官网](https://agentskills.io)