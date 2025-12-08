
---
title: treesj
---

### [Wansmer treesj](https://github.com/Wansmer/treesj)

**核心内容总结：**  
该项目提供一个名为 **TreeSJ** 的库，用于操作和格式化树状结构节点（基于 Neovim 的 Treesitter 插件）。其核心功能包括：  
1. **节点操作**：支持创建、删除、交换子节点，检查节点状态（如是否为首个/末尾节点、是否需忽略格式化等）。  
2. **文本格式化**：提供 `format_tree` 和 `format_resulted_lines` 自定义函数，实现递归格式化、文本更新、括号包裹等操作。  
3. **递归处理**：支持递归模式下的子节点遍历与格式化，确保结构完整性。  
4. **API 方法**：包含 `has_children`、`create_child`、`update_children`、`wrap` 等方法，用于灵活管理树状结构。  

**使用方法**：  
- 通过 `TreeSJ:create_child` 创建节点，`update_text` 修改文本，`wrap` 添加包裹元素。  
- 使用 `format_tree` 自定义逻辑处理节点格式，结合 `preset` 配置（如 `split`/`join` 模式）控制行为。  
- 利用 `iter_children`、`children` 等方法遍历和过滤子节点。  

**主要特性**：  
- 支持递归格式化与子节点状态检查（如 `will_be_formatted`、`is_ignore`）。  
- 提供 `preset` 配置功能，允许按需定义格式化规则。  
- 兼容 Treesitter 节点操作，通过 `tsnode` 方法获取原生节点或模拟对象。