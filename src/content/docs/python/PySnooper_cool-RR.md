
---
title: PySnooper
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/cool-RR/PySnooper?style=social) ](https://github.com/cool-RR/PySnooper)
### [cool-RR PySnooper](https://github.com/cool-RR/PySnooper)

**PySnooper核心内容总结：**  

**功能**：PySnooper是一个自动化调试工具，通过添加装饰器替代传统`print`语句，记录函数执行过程中的代码行、变量变化及执行时间，帮助定位代码问题。  

**使用方法**：  
1. 用`@pysnooper.snoop()`装饰目标函数，或用`with pysnooper.snoop():`包裹代码段。  
2. 输出默认显示在终端，也可通过参数指定输出到文件（如`@pysnooper.snoop('/path/log.txt')`）。  

**主要特性**：  
- 自动追踪变量值变化及执行步骤，无需手动添加`print`。  
- 支持监视非局部变量的表达式（如`watch=('foo.bar', 'self.x["whatever"]')`）。  
- 可设置`depth`参数追踪被调用函数的调试信息。  
- 适用于大型代码库，无需复杂调试器配置。  

**安装**：通过`pip install pysnooper`或Conda等包管理工具安装。