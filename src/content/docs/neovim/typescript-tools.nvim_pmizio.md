
---
title: typescript-tools.nvim
---

### [pmizio typescript-tools.nvim](https://github.com/pmizio/typescript-tools.nvim)

**项目核心内容总结：**

**功能**  
typescript-tools.nvim 是一个为 NeoVim 提供的 TypeScript 工具插件，通过原生 Tsserver 协议与 TypeScript 服务器通信，替代传统的 `typescript-language-server`，解决大型项目中语言服务器性能差、易崩溃的问题。支持代码补全、诊断、重构（如提取变量/函数）、样式组件（styled-components）智能提示等功能。

**主要特性**  
- 使用原生 Tsserver 协议，性能更快  
- 支持 TypeScript 4.0 及以上版本，兼容多个 Tsserver 实例  
- 支持本地/全局安装的 TypeScript，可通过 Mason 安装 tsserver  
- 提供代码整理（如排序/删除无用导入、修复错误等）的自定义命令  
- 支持 LSP 方法：补全、跳转定义、重命名、诊断、代码动作等（部分功能需 TypeScript 版本支持）  

**使用方法**  
1. **安装**：通过 `lazy.nvim` 或 `packer.nvim` 安装，需移除原有 `typescript-language-server` 配置。  
2. **配置**：在 `setup` 中设置诊断服务器、代码动作选项、tsserver 插件（如 styled-components 需全局安装 `@styled/typescript-styled-plugin`）。  
3. **使用命令**：如 `TSToolsOrganizeImports`（整理导入）、`TSToolsRenameFile`（重命名文件并更新引用）等。  

**注意事项**  
- 项目为测试版，可能存在 Bug  
- 需 NeoVim 0.11.0+、`plenary.nvim` 等依赖  
- 某些 LSP 方法（如 `workspace/applyEdit`）暂不支持