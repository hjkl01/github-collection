
---
title: neotest-go
---

### [nvim-neotest neotest-go](https://github.com/nvim-neotest/neotest-go)  ![GitHub Repo stars](https://img.shields.io/github/stars/nvim-neotest/neotest-go?style=social)

该项目是 Neotest 框架的 Go 语言适配器，专为 Neovim 编辑器设计，用于在编辑环境中运行和管理 Go 测试。核心功能包括：
- 集成 Neotest 框架并配置 Go 测试适配器；
- 支持运行单个测试函数、测试文件、指定目录或整个项目测试套件；
- 支持向 `go test` 命令传递额外参数（如超时、竞争检测等），并支持递归运行测试；
- 可选配置诊断信息的虚拟文本显示，以优化测试错误信息的可读性。