### [pwntester octo.nvim](https://github.com/pwntester/octo.nvim)  ![GitHub Repo stars](https://img.shields.io/github/stars/pwntester/octo.nvim?style=social)

该项目是一个用于 Neovim 的插件，名为 **octo.nvim**，其主要功能是允许用户在不离开编辑器的情况下，直接在编辑器中编辑和审查 GitHub 上的 issues（问题）、pull requests（拉取请求）和 discussions（讨论）。以下是其核心功能总结：

1. **编辑 GitHub issues 和 PRs**  
   - 可以像编辑普通文件一样编辑 issue 或 PR 的标题、正文和评论。
   - 使用 `:w` 命令保存后，内容会同步到 GitHub 上。

2. **评论和反应管理**  
   - 添加、修改或删除评论。
   - 添加或删除 issue/PR 的标签、反应（如点赞、火箭等）、分配人、项目卡片、审阅者等。

3. **PR 审查功能**  
   - 支持在编辑器中对 PR 进行审查（Review）。
   - 提供文件差异面板，可以添加评论、建议或标记为已解决。
   - 支持多种审查动作（如批准、请求修改、提交评论等）。

4. **搜索与过滤**  
   - 支持实时搜索 GitHub issues 和 PRs。
   - 提供多种过滤条件（如作者、标签、状态等）。

5. **快捷命令与 URL 支持**  
   - 支持通过 `Octo` 命令直接打开特定的 issue 或 PR。
   - 支持通过 `octo://` URL 直接访问 GitHub 内容。
   - 支持 GitHub Enterprise 的 URL。

6. **集成 GitHub CLI**  
   - 使用 `gh` 命令行工具进行更深入的 GitHub 操作。
   - 支持 Projects v2（需配置相应权限）。

7. **自定义配置**  
   - 提供丰富的配置选项，包括界面显示、快捷键、颜色主题等。
   - 可以自定义 picker（如 telescope、fzf-lua 等）来选择 issue/PR。

8. **通知与自动刷新**  
   - 可以查看 GitHub 通知。
   - 支持自动轮询以检测远程更改。

9. **多仓库与多 GitHub 实例支持**  
   - 支持在多个 GitHub 实例（如 GitHub.com 和 GitHub Enterprise）之间切换。

10. **补全与语法高亮**  
    - 提供对 issue/pr 和用户名称的自动补全功能。
    - 支持 Markdown 语法高亮。

总结：octo.nvim 是一个强大的 Neovim 插件，旨在提升开发者在处理 GitHub 上的 issues、PRs 和 discussions 时的效率和体验，所有操作都可以在编辑器内完成，无需频繁切换到浏览器。