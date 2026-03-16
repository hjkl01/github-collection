### [cool-RR PySnooper](https://github.com/cool-RR/PySnooper)  ![GitHub Repo stars](https://img.shields.io/github/stars/cool-RR/PySnooper?style=social)

PySnooper 是一款 Python 调试工具，旨在替代手动插入 print 语句进行调试。通过为函数添加装饰器 `@pysnooper.snoop()` 或使用 `with` 语句块包裹代码，它能自动记录函数的逐行执行日志、变量赋值及时间戳。支持将调试输出重定向至文件、监控非局部变量表达式以及设定调用栈追踪深度。该工具无需复杂配置，安装即可直接用于快速排查代码问题。