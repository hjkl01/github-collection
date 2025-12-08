
---
title: nvim-config
---

### [jdhao nvim-config](https://github.com/jdhao/nvim-config)

该项目是一个高度定制化的 **Neovim 配置方案**，支持 **Linux、macOS 和 Windows** 平台，提供以下核心功能和特性：

---

### **核心功能**
1. **插件集成**  
   - 使用 **Lazy.nvim** 管理插件，支持代码补全（nvim-cmp）、LSP（nvim-lspconfig）、Git 操作（vim-fugitive）、文件搜索（fzf）、代码折叠（nvim-ufo）等功能。
   - 内置 **快捷键系统**，例如 `<leader>ff` 快速搜索文件、`<F9>` 编译运行代码等（完整快捷键列表见文档）。

2. **自定义命令**  
   - 提供 `Redir`（捕获命令输出）、`Edit`（批量编辑文件）、`Datetime`（时间处理）、`JSONFormat`（格式化 JSON）等实用命令。

3. **多平台兼容**  
   - 支持跨平台使用，提供针对 **Windows、Linux 和 macOS** 的配置说明。

---

### **使用方法**
1. **安装依赖**  
   - 按照 `docs/README.md` 指南安装 Neovim 及相关依赖。
2. **配置初始化**  
   - 通过 `init.lua` 和 `ginit.vim` 初始化配置，**不建议直接克隆使用**，而是根据需求复制部分配置到个人项目中。
3. **快捷键与命令**  
   - 使用预设快捷键（如 `<leader>gs` 查看 Git 状态）或自定义命令（如 `Edit *.vim` 批量编辑文件）提升效率。

---

### **主要特性**
- **高度可定制**：通过插件和快捷键灵活调整工作流。
- **跨平台支持**：适配主流操作系统。
- **开发效率工具**：集成代码补全、LSP、Git 操作、快速搜索等。
- **文档完善**：提供详细安装指南（`docs/README.md`）及资源推荐（`nvim_resources.md`）。