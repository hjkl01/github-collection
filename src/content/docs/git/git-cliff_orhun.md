
---
title: git-cliff
---

### [orhun git-cliff](https://github.com/orhun/git-cliff)

**项目核心内容总结：**  
git-cliff 是一个基于 Git 历史生成变更日志（changelog）的工具，支持通过 [常规提交规范](https://git-cliff.org/docs/configuration/git#conventional_commits) 和正则表达式驱动的 [自定义解析器](https://git-cliff.org/docs/configuration/git#commit_parsers) 自动提取提交信息。用户可通过配置文件自定义变更日志模板，灵活适配不同格式需求。  

**主要特性：**  
- 从 Git 提交记录自动生成结构化变更日志  
- 支持常规提交规范（如 `feat`, `fix`, `chore` 等类型）  
- 提供正则表达式解析器，兼容非标准提交格式  
- 可通过配置文件定制输出模板（如 Markdown、JSON 等）  
- 集成 GitHub Actions、Docker 等 CI/CD 工具链  

**使用方法：**  
1. 安装工具（支持 Cargo、Homebrew 等方式）  
2. 配置 `git-cliff.toml` 文件定义解析规则和模板  
3. 执行命令生成变更日志（如 `git-cliff --output CHANGELOG.md`）  

**适用场景：**  
适用于需要自动化维护项目变更日志的开源项目或企业项目，尤其适合采用语义化版本管理（SemVer）的团队。