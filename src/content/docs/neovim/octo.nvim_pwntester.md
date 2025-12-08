
---
title: octo.nvim
---

### [pwntester octo.nvim](https://github.com/pwntester/octo.nvim)

**项目核心内容总结：**

octo.nvim 是一个 Vim 插件，用于在 GitHub 上管理 Issues、Pull Requests（PR）和项目。其主要功能包括：

1. **核心功能**  
   - 浏览、创建、评论 Issues/PR，查看详细信息（如状态、评论、测试结果）；  
   - 管理 GitHub Projects（支持 Projects V2）；  
   - 通过搜索功能查找 Issues/PR（支持 GitHub 搜索语法）；  
   - 提供 PR 审查面板，显示代码差异和审查状态。

2. **主要特性**  
   - 实时同步 GitHub 数据；  
   - 丰富的快捷键和交互式操作（如快速创建 Issue/PR）；  
   - 可自定义的高亮主题（如状态颜色、气泡样式）；  
   - 支持与 `gh` CLI 工具集成，需配置 GitHub 认证；  
   - 兼容 TreeSitter 语法解析，提升 Markdown 高亮效果。

3. **使用方法**  
   - 安装后通过 `:Octo` 命令打开界面；  
   - 使用搜索功能（如 `:Octo search is:pr author:xxx`）；  
   - 配置 `gh` 认证（需 `read:project` 权限以启用 Projects V2）；  
   - 自定义高亮规则（如禁用气泡样式）。

**注意事项：**  
- 部分功能（如 Projects V2）需 GitHub Token 拥有 `read:project` 权限；  
- 若遇到认证错误，需通过 `gh auth login` 配置有效凭据；  
- 可通过 `vim.keymap.set` 自定义 `@` 和 `#` 的自动补全行为；  
- 需确保 `.git/config` 中的 SSH 别名正确映射到 GitHub。