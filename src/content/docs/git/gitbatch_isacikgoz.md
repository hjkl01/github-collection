
---
title: gitbatch
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/isacikgoz/gitbatch?style=social) ](https://github.com/isacikgoz/gitbatch)
### [isacikgoz gitbatch](https://github.com/isacikgoz/gitbatch)

**核心内容总结：**

gitbatch 是一款用于批量管理多个 Git 仓库的工具，支持批量操作（如拉取更新）及单个仓库的精细化管理（如 add/reset、stash、commit 等）。  
**使用方法**：安装 Go 后通过 `go get` 或 `go install` 安装，MacOS 可用 Homebrew；在仓库父目录运行 `gitbatch` 命令，使用 `--help` 查看选项。  
**主要特性**：基于 go-git 库实现 Git 接口，部分功能仍依赖传统 Git 命令；未来计划完善 go-git 集成、增加推送功能及改进测试。