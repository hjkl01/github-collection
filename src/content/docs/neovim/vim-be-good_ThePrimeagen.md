
---
title: vim-be-good
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/ThePrimeagen/vim-be-good?style=social) ](https://github.com/ThePrimeagen/vim-be-good)
### [ThePrimeagen vim-be-good](https://github.com/ThePrimeagen/vim-be-good)

**项目核心内容总结：**

**功能**  
Vim-be-good 是一个通过游戏化练习提升 Vim 操作技能的 Neovim 插件，包含以下游戏模式：  
- **relative**：通过相对跳转删除指定行；  
- **ci{**：用 `ci[` 或 `ci{` 替换括号内内容为 "bar"；  
- **whackamole**：快速定位并切换特定字符大小写。  

**使用方法**  
1. **安装**：使用 Neovim 5.x 及插件管理器（如 `Plug 'ThePrimeagen/vim-be-good'`）安装；  
2. **Docker**：通过 `docker run` 启动预配置镜像（分稳定版和最新版）；  
3. **启动**：在空文件中执行 `:VimBeGood` 选择游戏，按提示操作。  

**主要特性**  
- 支持自定义游戏参数（如难度偏移量 `vim_be_good_delete_me_offset`）；  
- 提供日志记录功能（设置 `g:vim_be_good_log_file = 1` 生成日志用于问题反馈）；  
- 开发者可贡献新游戏模式（通过提交 Issue 或 PR）。  

**注意事项**  
- 代码为直播开发，可能存在不完善；  
- 游戏难度目前仅部分支持；  
- 必须在空文件中使用，否则报错。