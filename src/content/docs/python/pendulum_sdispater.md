
---
title: pendulum
---

### [sdispater pendulum](https://github.com/sdispater/pendulum)  ![GitHub Repo stars](https://img.shields.io/github/stars/sdispater/pendulum?style=social)

Pendulum 是一款 Python 日期时间库，旨在简化日期时间操作并支持 Python 3.10 及以上版本。作为标准 datetime 类的替代品（继承自 datetime），它提供更直观易用的 API。主要功能包括：无缝切换时区、直观的时间加减运算、生成人类可读的时间差描述、自动正确处理夏令时过渡及日期归一化，并强制所有实例均为时区感知（默认 UTC）。此外，它改进了标准的 timedelta 类。在 sqlite3、mysqlclient、PyMySQL 及 Django 等特定场景下，可能需要注册适配器以解决类型检查或格式化兼容性问题。