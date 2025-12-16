
---
title: schedule
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/dbader/schedule?style=social) ](https://github.com/dbader/schedule)
### [dbader schedule](https://github.com/dbader/schedule)

**项目核心内容总结：**  
`schedule` 是一个为人类设计的 Python 定时任务调度库，支持以简洁语法周期性运行函数或可调用对象。  

**功能与特性：**  
- 提供简单易用的 API，无需额外进程即可实现进程内调度；  
- 轻量无外部依赖，测试覆盖率高；  
- 支持 Python 3.7 至 3.12 多个版本；  
- 可定义任务频率（如每秒、分钟、小时、每天特定时间、每周特定日期等），并支持传递参数；  
- 示例代码通过 `schedule.every().xxx.do(函数)` 设置任务，配合 `while True` 循环持续运行。  

**使用方法：**  
1. 安装：`pip install schedule`；  
2. 编写任务函数，通过 `schedule.every().xxx.do(函数)` 设置周期；  
3. 使用 `schedule.run_pending()` 和 `time.sleep()` 持续运行调度器。