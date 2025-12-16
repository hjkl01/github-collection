
---
title: fff.nvim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/dmtrKovalenko/fff.nvim?style=social) ](https://github.com/dmtrKovalenko/fff.nvim)
### [dmtrKovalenko fff.nvim](https://github.com/dmtrKovalenko/fff.nvim)

**FFF.nvim 核心内容总结：**

**项目功能**  
FFF.nvim 是 Neovim 的智能模糊文件选择器，支持快速、拼写容错的文件搜索，集成 Git 状态，通过后台维护的文件索引实现超快搜索（50k 文件代码库搜索<10ms），支持图片预览（需 snacks.nvim），并提供懒加载初始化。

**使用方法**  
- **安装**：支持 `lazy.nvim` 和 `vim.pack`，需 Neovim 0.10+ 及 Rustup（需 nightly 工具链）。  
- **配置**：提供默认配置，可自定义搜索路径、布局、预览设置、快捷键、高亮样式等。  
- **操作**：通过 `:FFFFind` 命令或快捷键（如 `ff`）打开文件选择器，支持多目录搜索、Git 根目录搜索、缓存清理等。

**主要特性**  
- 无需额外配置即可使用；  
- 拼写容错模糊搜索（基于 Frizbee 算法）；  
- Git 状态集成（如修改时间）；  
- 后台索引确保高速搜索；  
- 支持图片预览及动态加载大文件内容；  
- 智能初始化（懒加载）；  
- 可调试搜索评分，支持日志分析。  

**常见问题解决**  
- 通过 `:FFFHealth` 检查依赖状态；  
- 使用 `:FFFOpenLog` 查看日志；  
- 若搜索失败，手动运行 `:FFFScan` 或检查 `base_path` 配置；  
- 图片预览需终端支持（如 Kitty）或安装 `chafa` 等工具。