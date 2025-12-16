
---
title: pendulum
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/sdispater/pendulum?style=social) ](https://github.com/sdispater/pendulum)
### [sdispater pendulum](https://github.com/sdispater/pendulum)

**核心内容总结：**  
Pendulum 是一个 Python 日期时间处理库，旨在简化复杂时间操作。其核心功能包括：  
1. **时区处理**：支持时区切换（如 `now('Europe/Paris')` 转换为 UTC），自动处理夏令时转换问题。  
2. **时间操作**：提供直观的增减时间方法（如 `add(days=1)`、`subtract(weeks=1)`）及时间差计算（如 `diff_for_humans()` 显示“2 分钟前”）。  
3. **兼容性**：作为 `datetime` 的替代品（继承自 `datetime`），所有实例默认带时区（UTC），可无缝替换代码中的 `datetime`。  
4. **标准化处理**：自动修正非法时间（如跳过时间的标准化）。  

**使用方法**：  
通过 `pendulum.now()` 获取当前时间，结合 `in_timezone()`、`add()`、`subtract()` 等方法操作时间，使用 `diff_for_humans()` 生成人性化时间差描述。  

**注意事项**：  
与部分库（如 `sqlite3`、`mysqlclient`）兼容时需注册自定义适配器，Django 需要重写 `DateTimeField` 以适配 Pendulum 的时区特性。