
---
title: mypy
---

### [python mypy](https://github.com/python/mypy)

**核心内容总结：**  
Mypy 是 Python 的静态类型检查工具，用于在代码运行前发现类型错误。它基于 PEP 484 的类型提示，支持渐进式类型检查，允许逐步添加类型注解而不影响代码运行。主要特性包括类型推断、泛型、联合类型、结构子类型等。  

**使用方法：**  
通过 `pip install mypy` 安装，使用 `mypy PROGRAM` 命令检查代码，或通过 `python3 PROGRAM` 运行代码。大型项目可使用 `dmypy run` 提升检查速度。支持集成到主流 IDE（如 VS Code、PyCharm 等）。  

**主要特性：**  
- 支持复杂类型系统（泛型、元组、联合类型等）；  
- 渐进式类型检查，兼容动态类型；  
- 提供详细的错误提示和文档（如常见问题、错误代码列表）；  
- 可通过在线工具（如 mypy-play.net）快速体验。