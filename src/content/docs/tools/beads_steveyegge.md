
---
title: beads
---

### [steveyegge beads](https://github.com/steveyegge/beads)  ![GitHub Repo stars](https://img.shields.io/github/stars/steveyegge/beads?style=social)

**项目核心内容总结：**  
Beads 是一个基于 Git 的分布式图式任务跟踪工具，为 AI 代理提供持久化、结构化的记忆管理，通过依赖感知的图结构替代传统 Markdown 计划，支持长期任务管理与上下文保留。

**功能与使用方法：**  
- **安装**：通过 `curl` 脚本、npm、Homebrew 或 Go 安装。  
- **初始化**：运行 `bd init` 创建本地存储，`bd init --stealth` 可隐藏文件不提交到主仓库。  
- **任务管理**：使用 `bd create` 创建任务，`bd dep add` 建立依赖关系，`bd ready` 查看可执行任务，`bd show` 查看任务详情。

**主要特性：**  
1. **Git 作为数据库**：任务以 JSONL 格式存储于 `.beads/`，支持版本控制、分支与合并。  
2. **代理优化**：JSON 输出、依赖追踪、自动识别无阻塞任务。  
3. **无冲突设计**：通过哈希 ID（如 `bd-a1b2`）避免多代理/分支合并冲突。  
4. **高效性能**：SQLite 本地缓存加速操作，后台守护进程自动同步。  
5. **智能压缩**：通过“记忆衰减”自动汇总已关闭任务，节省上下文空间。