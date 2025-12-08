
---
title: better-exceptions
---

### [Qix- better-exceptions](https://github.com/Qix-/better-exceptions)

**项目功能**  
`better-exceptions` 是一个 Python 库，用于美化异常信息，自动提供更详细、易读的错误提示，帮助开发者快速定位问题。

**使用方法**  
1. 安装：通过 `pip install better_exceptions` 安装。  
2. 启用：设置环境变量 `BETTER_EXCEPTIONS=1`（Linux/macOS 使用 `export`，Windows 使用 `setx`）。  
3. 交互式 shell：运行 `python -m better_exceptions` 进入增强版 Python 环境。  

**主要特性**  
- 自动美化异常输出，显示文件路径、代码上下文、变量值等信息。  
- 支持自定义输出长度（如 `better_exceptions.MAX_LENGTH = None` 禁用截断）。  
- 集成 `unittest`：通过 Monkey Patch 替换默认异常格式化方法。  
- Django 支持：通过中间件和日志配置实现异常美化，避免重复日志输出。  
- 生产环境需关闭 `BETTER_EXCEPTIONS` 防止敏感信息泄露。  

**注意事项**  
- 与 `python3-apport` 等库可能冲突，需排查并卸载干扰组件。  
- 若未生效，检查环境变量是否设置正确或手动调用 `better_exceptions.hook()`。