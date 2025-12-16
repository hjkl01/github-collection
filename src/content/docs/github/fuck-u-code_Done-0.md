
---
title: fuck-u-code
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/Done-0/fuck-u-code?style=social) ](https://github.com/Done-0/fuck-u-code)
### [Done-0 fuck-u-code](https://github.com/Done-0/fuck-u-code)

**项目核心内容总结：**

**功能**  
fuck-u-code 是一款用于分析代码质量的工具，通过“屎山指数”（0-100分）和七维度检测（复杂度、函数长度、注释率、错误处理、命名、重复度、结构），以幽默方式指出代码的劣质程度，支持 Go、JS/TS、Python、Java、C/C++ 等多语言。

**主要特性**  
- 彩色终端报告与 Markdown 格式输出，便于集成至文档或 CI/CD 流程。  
- 支持本地项目或 Git 仓库（自动克隆）分析，分析后自动清理临时文件。  
- 可配置模式（摘要/详细）、排除路径及报告语言（中文/英文/俄文）。  

**使用方法**  
1. **安装**：通过 Go 安装、源码构建或 Docker 镜像构建。  
2. **基本命令**：  
   - 分析本地项目：`fuck-u-code /path/to/project`  
   - 分析 Git 仓库：`fuck-u-code https://github.com/user/repo.git`  
3. **常用选项**：  
   - `--verbose` 查看详细报告，`--top N` 显示最烂前 N 个文件，`--markdown` 输出 Markdown 报告，`--exclude` 排除指定路径。  

**其他**  
- 默认排除 `node_modules`、`dist`、`vendor` 等非代码目录。  
- 若命令未找到，需将 Go 的 `GOPATH/bin` 加入系统 `PATH`。