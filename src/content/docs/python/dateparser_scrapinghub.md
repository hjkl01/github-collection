
---
title: dateparser
---

### [scrapinghub dateparser](https://github.com/scrapinghub/dateparser)

**核心内容总结：**  
**项目功能**：一个用于解析人类可读日期的 Python 库，支持绝对日期、相对日期（如“两周前”）、时间戳、多语言（200+ 种语言）及非公历历法（如伊斯兰历、波斯历），可处理时区信息，并能从文本中搜索日期。  

**使用方法**：通过 `dateparser.parse()` 函数直接解析日期字符串，支持自定义设置（如语言、日期格式、时区等）。例如：`dateparser.parse('tomorrow')` 或 `dateparser.parse('2023-01-01', settings={'DATE_ORDER': 'YMD'})`。  

**主要特性**：  
- 支持 200+ 种语言及自动语言检测  
- 自定义设置（如日期格式、时区、解析器优先级）  
- 支持非公历历法（需安装额外依赖）  
- 从文本中提取日期（如“过去一个月”）  
- 处理时区缩写（如“EST”）和 UTC 偏移（如“+0500”）  

**安装方式**：`pip install dateparser`；若需支持非公历历法，安装 `dateparser[calendars]`。  

**常见用途**：网页抓取、物联网数据处理、日志分析、用户自然语言交互（如“3 天前”）。  

**相关项目**：价格解析器（price-parser）、数字解析器（number-parser）、爬虫框架（Scrapy）。  

**许可证**：BSD 3-Clause。