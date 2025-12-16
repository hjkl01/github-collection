
---
title: click
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/pallets/click?style=social) ](https://github.com/pallets/click)
### [pallets click](https://github.com/pallets/click)

**核心内容总结：**  
Click 是一个用于创建命令行接口（CLI）的 Python 库，通过装饰器和简洁代码实现功能，支持高度可配置的 CLI 工具开发。其核心特性包括：  
1. **命令嵌套**：支持任意层级的子命令嵌套；  
2. **自动帮助页**：自动生成详细的帮助信息；  
3. **延迟加载**：运行时按需加载子命令，提升性能。  

**使用方法**：通过 `@click.command()` 和 `@click.option()` 等装饰器定义命令和参数，示例代码可快速实现带参数的 CLI 程序（如 `hello.py` 示例）。