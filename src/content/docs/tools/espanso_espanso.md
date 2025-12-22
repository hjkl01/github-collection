
---
title: espanso
---

### [espanso espanso](https://github.com/espanso/espanso)  ![GitHub Repo stars](https://img.shields.io/github/stars/espanso/espanso?style=social)

**项目核心内容总结**：

Espanso 是一个用 Rust 编写的跨平台文本扩展工具，支持 Windows、macOS 和 Linux 系统。其功能是通过检测用户输入的关键词，自动替换为预设内容（如文本、代码、表情、图片或执行脚本），可大幅减少重复输入，提升效率。

**主要特性**：
- **跨平台兼容**：支持 Windows、macOS 和 Linux（含 Wayland 实验性支持）。
- **隐私保护**：所有操作本地完成，无数据上传或追踪。
- **灵活扩展**：支持表情符号、图片、日期、正则表达式触发、自定义脚本及 Shell 命令。
- **搜索功能**：内置搜索栏可快速查找替换内容。
- **配置自由**：通过 YAML 文件定义触发词与替换内容，支持分场景配置。
- **社区支持**：提供官方文档、Discord 群组及 Reddit 论坛，支持社区包扩展。

**使用方法**：
在 YAML 配置文件中定义规则，例如：
```yaml
matches:
  - trigger: ":hello"
    replace: "Hi There!"
  - triggers: [":test1", ":test2"]
    replace: "These both expand to the same thing"
```  
保存后，输入触发词（如 `:hello`）即可自动替换为设定内容。