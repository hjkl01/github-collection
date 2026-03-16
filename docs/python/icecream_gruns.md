### [gruns icecream](https://github.com/gruns/icecream)  ![GitHub Repo stars](https://img.shields.io/github/stars/gruns/icecream?style=social)

IceCream 是一个 Python 调试工具，通过 `ic()` 函数替代 `print()` 增强调试体验。核心功能如下：

1. **增强打印**：自动显示变量表达式及其计算值，支持数据结构格式化与语法高亮。
2. **上下文追踪**：可选显示调用位置（文件名、行号、父函数名）。
3. **非侵入式**：返回输入参数值，可无缝嵌入现有代码逻辑。
4. **灵活配置**：支持全局安装（免导入）、自定义输出格式、启用/禁用输出及自定义序列化。
5. **兼容性**：支持 Python 3 和 PyPy3。