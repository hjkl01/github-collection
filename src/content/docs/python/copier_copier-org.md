
---
title: copier
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/copier-org/copier?style=social) ](https://github.com/copier-org/copier)
### [copier-org copier](https://github.com/copier-org/copier)

**项目核心内容总结：**  

**功能**：Copier 是一个用于渲染项目模板的库和命令行工具，支持从本地路径或 Git 仓库生成项目结构，动态替换文件中的变量，并避免意外覆盖已有文件。  

**使用方法**：  
1. **安装**：需 Python 3.10+ 和 Git 2.27+，可通过 `pipx`、`uv`、`pip` 或 Homebrew 安装。  
2. **模板创建**：在模板目录中编写 `copier.yml` 定义变量，使用 Jinja2 语法标记需替换的文件（如 `{{variable}}`）。  
3. **生成项目**：  
   - 命令行：`copier copy <模板路径> <目标路径>`  
   - Python 代码：调用 `copier.run_copy()`，支持本地路径或 Git URL（如 `gh:username/repo.git`）。  

**主要特性**：  
- 支持本地路径和 Git 仓库作为模板来源。  
- 动态替换文本文件中的变量，兼容多种文件类型。  
- 智能处理文件生成，避免覆盖已有文件（除非明确允许）。  
- 提供问答式配置（`copier.yml`），生成项目时交互式填写变量。  
- 可扩展为复杂模板，适用于代码 scaffolding 和项目生命周期管理。  

**适用场景**：  
- 模板开发者：快速构建可复用的项目模板。  
- 开发者：通过模板快速初始化新项目或更新现有项目结构。