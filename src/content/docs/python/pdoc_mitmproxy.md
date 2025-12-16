
---
title: pdoc
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/mitmproxy/pdoc?style=social) ](https://github.com/mitmproxy/pdoc)
### [mitmproxy pdoc](https://github.com/mitmproxy/pdoc)

**项目核心内容总结：**  
pdoc 是一个用于生成 Python 项目 API 文档的工具，支持 Markdown 格式，兼容 Python 3.10 及以上版本。  

**使用方法：**  
通过 `pip install pdoc` 安装后，运行 `pdoc your_python_module` 或 `pdoc ./my_project.py` 生成文档。支持内置 Web 服务器实时预览，也可导出为独立 HTML 文件。  

**主要特性：**  
1. 支持类型注解、现代 Python 特性及 numpydoc/Google 风格注释；  
2. 自动链接文档中的标识符，尊重 `__all__` 变量；  
3. 提取构造函数的类型注解和 docstring，解析前向引用；  
4. 自定义 HTML 模板，无需依赖其他工具；  
5. 提供命令行参数查看帮助信息或生成文档。  

**注意事项：**  
pdoc 与同名项目 pdoc3 无关联，强调社区友好和避免使用纳粹符号。