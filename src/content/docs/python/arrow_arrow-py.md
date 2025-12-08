
---
title: arrow
---

### [arrow-py arrow](https://github.com/arrow-py/arrow)

**项目核心内容总结：**

**功能**  
Arrow 是 Python 的日期时间处理库，提供更人性化的操作方式，替代标准库 `datetime`，支持创建、转换、格式化日期时间及时间戳。

**使用方法**  
- 安装：通过 `pip install -U arrow` 安装  
- 示例：  
  - 创建时间：`arrow.get('2013-05-11T21:23:58.970460+07:00')`  
  - 获取当前时间：`arrow.utcnow()`  
  - 时区转换：`utc.to('US/Pacific')`  
  - 格式化输出：`local.format('YYYY-MM-DD HH:mm:ss ZZ')`  
  - 人性化显示：`local.humanize()`  

**主要特性**  
1. 支持 Python 3.8+，默认使用 UTC 和时区感知  
2. 自动解析格式化字符串，支持 ISO 8601 标准  
3. 提供 `shift` 方法实现相对时间偏移（如小时、周）  
4. 支持 `dateutil`、`pytz` 和 `ZoneInfo` 时区对象  
5. 可生成时间范围、区间及时间框架的上下限  
6. 支持多语言本地化显示（如韩语）  
7. 可扩展为自定义类型，兼容 PEP 484 类型提示