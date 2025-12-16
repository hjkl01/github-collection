
---
title: leetcode.nvim
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/kawre/leetcode.nvim?style=social) ](https://github.com/kawre/leetcode.nvim)
### [kawre leetcode.nvim](https://github.com/kawre/leetcode.nvim)

### 项目核心内容总结

**项目功能**  
`leetcode.nvim` 是一个用于在 Neovim 中解决 LeetCode 题目的插件，提供以下功能：  
- **导航仪表板**：直观的界面管理题目和状态。  
- **问题描述优化**：格式化显示题目描述，提升可读性。  
- **统计信息**：在 Neovim 中查看 LeetCode 个人资料数据。  
- **每日/随机题目**：支持随机题目和每日一题功能。  
- **性能优化**：通过缓存机制提升加载速度。  

**使用方法**  
- **启动方式**：  
  1. 命令行启动：`nvim leetcode.nvim`。  
  2. 使用 `:Leet` 命令（需 Neovim 无其他缓冲区，或启用非独立模式）。  
- **关键命令**：  
  - `:Leet list`：筛选题目状态、难度、标签。  
  - `:Leet random`：随机选择题目（支持条件筛选）。  
  - `:Leet desc`：切换题目描述显示。  
  - `:Leet cookie update`：更新登录 Cookie。  

**主要特性**  
- **灵活配置**：支持语言选择（如 Rust、Python）、存储路径、插件模式（独立/非独立）、主题自定义等。  
- **依赖管理**：需安装 Neovim 0.9.0+、Picker 插件（如 telescope.nvim、fzf-lua）、树状语法解析器（tree-sitter-html）等。  
- **兼容性**：支持 Windows（推荐使用 Cygwin）。  
- **问题处理**：提供常见问题解决方案，如 Cookie 过期、LSP 补全配置、测试用例切换等。  

**注意事项**  
- 登录时需复制浏览器请求头中的 Cookie，而非响应头的 `set-cookie`。  
- 若遇到 Cookie 过期错误，可能是 LeetCode 服务器限制访问，需等待或关闭 VPN。