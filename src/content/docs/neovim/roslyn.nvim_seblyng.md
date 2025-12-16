
---
title: roslyn.nvim
---

### [seblyng roslyn.nvim](https://github.com/seblyng/roslyn.nvim)

**项目核心内容总结：**

**项目功能**  
roslyn.nvim 是一个 Neovim 插件，用于集成 Roslyn 语言服务器（替代 OmniSharp），支持 C# 语言开发，包含 Razor/CSHTML 文件的智能感知。提供多解决方案管理、广域根目录检测、代码修复、复杂编辑等功能。

**使用方法**  
1. **安装**：通过 Mason 安装（需配置自定义注册表）或手动下载 Roslyn 语言服务器（通过 NuGet 包）。  
2. **配置 Neovim**：使用 `lazy.nvim` 等插件管理器加载插件，通过 `vim.lsp.config` 设置语言服务器参数。  
3. **命令**：支持 `:Roslyn target` 选择解决方案、`restart/start/stop` 控制服务器。

**主要特性**  
- 支持多解决方案管理及自动选择。  
- 广域根目录搜索（`broad_search` 选项）。  
- 支持 Razor/CSHTML 文件（替代 rzls.nvim）。  
- 提供代码修复、嵌套代码操作、复杂编辑功能。  
- 可配置文件监控模式（`filewatching`）、内联提示（Inlay Hints）、代码透镜（Code Lens）等。  

**依赖要求**  
- Neovim ≥ 0.11.0  
- .NET SDK 及 `dotnet` 命令  
- 本地安装 Roslyn 语言服务器