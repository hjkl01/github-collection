
---
title: posting
---

### [darrenburns posting](https://github.com/darrenburns/posting)

**核心内容总结：**  
Posting 是一款终端 HTTP 客户端工具，支持类似 Postman 的功能，可通过键盘高效操作。请求数据以 YAML 格式本地存储，便于版本控制。  

**主要特性：**  
- 支持跳转模式导航、环境变量、自动补全、语法高亮、Vim 快捷键、自定义键绑定和主题  
- 可运行 Python 代码、导入/导出 curl 命令、从 Postman/OpenAPI 导入请求  
- 提供命令面板、编辑器集成（$EDITOR/$PAGER）等扩展功能  

**使用方法：**  
通过 `uv tool install posting`（需先安装 uv）或 `pipx install posting` 安装，安装后直接运行 `posting` 命令启动。  

**技术实现：**  
基于 [Textual](https://github.com/textualize/textual) 开发，支持跨平台（MacOS/Linux/Windows）。