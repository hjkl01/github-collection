
---
title: neotest-go
---

### [nvim-neotest neotest-go](https://github.com/nvim-neotest/neotest-go)

**项目核心内容总结：**

**功能**  
neotest-go 是 Neotest 框架的 Go 语言适配器，用于在 Neovim 中运行 Go 单元测试，支持单个测试、文件、目录及整个项目测试。

**使用方法**  
1. **安装**：通过 packer 安装 neotest 及 neotest-go，配置 Lua 脚本启用插件。  
2. **运行测试**：  
   - 单个测试：悬停测试函数并调用 `require('neotest').run.run()`（注意：testify 测试方法不支持单个运行）。  
   - 文件/目录/项目：通过 `require('neotest').run.run({路径, extra_args = {参数}})` 指定范围及额外参数（如 `-race`）。  
3. **配置选项**：支持递归运行测试（`recursive_run = true`）、设置 `go test` 参数（如 `-count=1`）及优化诊断信息显示格式。

**主要特性**  
- 支持 Go 测试的多级运行（单个、文件、目录、项目）。  
- 可自定义 `go test` 参数及递归测试。  
- 优化诊断信息格式，提升 testify 错误信息可读性。  
- 提供实验性功能（如测试表支持）。