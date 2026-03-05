
---
title: sql-generator
---

### [liyupi sql-generator](https://github.com/liyupi/sql-generator)  ![GitHub Repo stars](https://img.shields.io/github/stars/liyupi/sql-generator?style=social)

这是一个结构化 SQL 生成器，通过 JSON 定义规则自动生成复杂 SQL，旨在提升编写效率与可维护性。

核心功能：
1. 结构复用：将 SQL 模块化，支持通过 @规则引用和嵌套，避免重复代码，便于维护。
2. 参数控制：支持变量替换（#{xxx}）及参数透传，支持局部 SQL 调试。
3. 调用分析：可视化展示 SQL 调用树和替换过程，便于理解引用关系。
4. 在线编辑：提供代码高亮、格式化及一键生成功能，支持浏览器端直接使用。

适用于大数据分析等存在大量相似 SQL 的复杂场景，也可作为通用重复代码生成器。