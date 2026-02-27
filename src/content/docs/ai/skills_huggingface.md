
---
title: skills
---

### [huggingface skills](https://github.com/huggingface/skills)  ![GitHub Repo stars](https://img.shields.io/github/stars/huggingface/skills?style=social)

**项目名称：Hugging Face Skills**

**项目功能：**  
该项目提供了一系列用于AI/ML任务的“技能（Skills）”，包括数据集创建、模型训练、评估等操作。这些技能可与主流的代码生成工具（如Claude Code、Codex、Gemini CLI、Cursor等）兼容，帮助用户更高效地完成机器学习工作流。

**使用方法：**  
- 每个技能是一个独立文件夹，包含操作指南、脚本和资源。
- 用户可通过不同工具安装技能：
  - **Claude Code**：通过插件市场安装。
  - **Codex**：通过`AGENTS.md`文件加载指令。
  - **Gemini CLI**：通过`gemini-extension.json`文件安装扩展。
  - **Cursor**：通过插件配置文件安装。
- 使用时只需告诉代码代理“使用某个技能”，代理会自动加载对应指令和脚本。

**主要特性：**  
- 提供多种现成技能（如模型训练、数据集管理、论文发布等）。
- 支持多平台兼容。
- 提供清晰的结构和标准化格式（如`SKILL.md`）。
- 用户可自定义和贡献新的技能。

**可用技能示例：**  
- `hugging-face-cli`：执行Hugging Face Hub操作。
- `hugging-face-model-trainer`：训练或微调语言模型。
- `hugging-face-evaluation`：添加和管理模型评估结果。
- `hugging-face-paper-publisher`：发布研究论文。
- `hugging-face-datasets`：创建和管理数据集。

**贡献方式：**  
- 复制现有技能文件夹并重命名。
- 修改`SKILL.md`中的名称和描述。
- 添加脚本和文档。
- 更新市场描述文件。
- 运行脚本发布并验证。