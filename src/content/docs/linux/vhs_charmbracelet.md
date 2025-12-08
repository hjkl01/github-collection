
---
title: vhs
---

### [charmbracelet vhs](https://github.com/charmbracelet/vhs)

**项目功能**  
VHS 是一个用于录制终端操作过程的工具，可生成 GIF 动画或 ASCII 艺术图，适用于演示、文档和自动化测试。支持通过脚本控制终端交互（如按键、等待输出、隐藏/显示录制），并能设置环境变量、复制粘贴文本、加载其他脚本。  

**使用方法**  
- 通过命令定义操作流程，例如：  
  - `Output example.gif`：指定输出文件。  
  - `Type "command"`：输入文本。  
  - `Enter`：按下回车键。  
  - `Wait /pattern/`：等待终端匹配指定正则表达式的内容。  
  - `Hide`/`Show`：暂停/恢复录制。  
- 使用 `Sleep` 暂停录制以等待操作完成（如加载状态）。  
- 通过 `Screenshot` 保存当前帧为 PNG 图像。  

**主要特性**  
- 支持生成 GIF、ASCII 艺术图及 PNG 截图。  
- 提供丰富的终端交互控制（如按键模拟、等待输出、环境变量设置）。  
- 可集成到 CI 流程，用于自动化测试和生成“黄金文件”进行对比验证。  
- 支持语法高亮（基于 Tree-sitter）。  
- 开源，采用 MIT 许可证。