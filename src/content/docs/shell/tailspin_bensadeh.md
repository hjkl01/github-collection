
---
title: tailspin
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/bensadeh/tailspin?style=social) ](https://github.com/bensadeh/tailspin)
### [bensadeh tailspin](https://github.com/bensadeh/tailspin)

### 核心内容总结

**项目功能**  
`tailspin` 是一个日志文件高亮工具，支持查看或实时跟踪（`tail`）任意格式的日志文件，无需配置即可自动识别并高亮数字、日期、IP 地址、UUID、URL、关键字等元素，所有高亮组支持自定义，且可与命令行工具集成。项目提供 Rust 语言的 crate 供扩展使用。

**主要特性**  
- 无需安装或配置，自动识别常见日志元素（如布尔值、null、日志等级、REST 动词等）；  
- 支持通过 `theme.toml` 文件自定义高亮样式；  
- 可通过命令行参数（如 `--highlight`、`--enable`、`--disable`）动态启用/禁用高亮组或添加自定义关键词；  
- 支持通过管道（`|`）接收其他命令的输出，或使用 `--exec` 参数执行命令并用 `less` 查看结果；  
- 使用 `less` 作为默认分页器，支持搜索、过滤、跟随模式（`-f`）等操作；  
- 允许通过环境变量 `TAILSPIN_PAGER` 替换默认分页器。

**使用方法**  
- 安装：通过 Homebrew、Cargo、包管理器（如 Archlinux）或从源码编译（需最新版 `less`）；  
- 基础用法：`tailspin [文件路径]`；  
- 高级功能：  
  - 实时跟踪日志：`tailspin -f [文件路径]`；  
  - 自定义高亮：`--highlight=红色:ERROR,WARNING`；  
  - 执行命令并查看输出：`tailspin --exec 'kubectl logs -f pod_name'`。