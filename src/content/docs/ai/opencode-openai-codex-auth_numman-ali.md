
---
title: opencode-openai-codex-auth
---

### [numman-ali opencode-openai-codex-auth](https://github.com/numman-ali/opencode-openai-codex-auth)  ![GitHub Repo stars](https://img.shields.io/github/stars/numman-ali/opencode-openai-codex-auth?style=social)

**项目核心内容总结：**

**功能**  
通过ChatGPT OAuth认证，一键接入GPT-5.x及Codex系列模型，提供代码生成、文本处理等能力，支持多模态输入。

**使用方法**  
1. 安装：`npx -y opencode-openai-codex-auth@latest`  
2. 登录：`opencode auth login`  
3. 运行命令：`opencode run "指令" --model=模型名 --variant=参数`（如`openai/gpt-5.2 --variant=medium`）  
4. 旧版本兼容：添加`--legacy`参数  
5. 卸载：`npx -y opencode-openai-codex-auth@latest --uninstall`

**主要特性**  
- 支持22种模型（如gpt-5.2、gpt-5.1-codex等）及多种参数变体（low/medium/high/xhigh）  
- 配置文件区分现代版（`config/opencode-modern.json`）与旧版（`config/opencode-legacy.json`）  
- 自动令牌刷新、错误提示、多模态输入  
- 仅需一次配置，适配所有模型  

**注意事项**  
仅限个人开发使用，生产环境需使用OpenAI官方API。