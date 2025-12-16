
---
title: dateutil
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/dateutil/dateutil?style=social) ](https://github.com/dateutil/dateutil)
### [dateutil dateutil](https://github.com/dateutil/dateutil)

**核心内容总结：**  
`dateutil` 是 Python 的 `datetime` 模块的扩展库，提供强大功能：  
- **功能**：支持相对时间差计算（如“下个月”“去年”）、基于 iCalendar 规则的日期重复计算、灵活解析任意格式的日期字符串、多种时区支持（包括 Olson 数据库、Windows 时区等）、复活节日期计算等。  
- **使用方法**：通过 `pip install python-dateutil` 安装，导入模块后即可使用（如 `from dateutil.relativedelta import relativedelta`）。  
- **主要特性**：  
  1. 精确计算日期间的相对增量（如“6 个月后”）；  
  2. 支持复杂重复规则（如“每月 13 日的星期五”）；  
  3. 自动解析多种格式的日期字符串；  
  4. 全面覆盖时区转换与本地化处理；  
  5. 内置世界时区数据库及复活节算法。  
- **示例**：可快速计算“下个 8 月 13 日星期五后的复活节日期与当前日期的间隔”。  

**注意事项**：  
- 安装时注意包名 `python-dateutil` 与导入名 `dateutil` 不同；  
- 部分功能依赖 Olson 时区数据库，需确保环境支持。