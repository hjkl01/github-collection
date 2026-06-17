### [no-mistakes](https://github.com/kunchenguid/no-mistakes) ![GitHub Repo stars](https://img.shields.io/github/stars/kunchenguid/no-mistakes?style=social)

## 项目功能总结

`no-mistakes` 是一个本地 git 代理工具，位于真实远程仓库前方。

**核心流程**：
将分支推送到 `no-mistakes` 而非 `origin` 时，它创建一个临时 worktree（不影响当前工作），运行 AI 驱动的验证流程（审查→测试→文档→lint），所有检查通过后才转发到上游并自动打开 PR。

**主要特性**：
- **非阻塞**：在隔离 worktree 中运行，不中断开发工作
- **兼容多 AI 代理**：支持 claude、codex、rovodev、opencode 等
- **人类主导**：安全修复自动应用，需要判断的内容由用户决定
- **默认生成干净 PR**：推送后自动打开 PR，自动修复 CI 失败

**三种触发方式**：
1. `git push no-mistakes` — 推送到代理远程
2. `no-mistakes` — TUI 交互界面
3. `/no-mistakes` — AI 代理调用技能