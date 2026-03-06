
---
title: sql-generator
---

### [liyupi sql-generator](https://github.com/liyupi/sql-generator)  ![GitHub Repo stars](https://img.shields.io/github/stars/liyupi/sql-generator?style=social)

本项目是一个结构化 SQL 生成器，通过 JSON 配置轻松生成复杂 SQL，旨在提高编写效率并降低维护成本。

核心功能：
1. **逻辑结构化**：将 SQL 拆分为模块化规则，像写大纲一样编写，实现代码复用，修改一处即可更新全局。
2. **灵活引用与传参**：支持 SQL 片段函数式调用（@ 规则名），支持参数透传、嵌套调用及动态变量（#{变量}）替换。
3. **可视化与调试**：提供在线编辑器，支持语法高亮、格式化，可直观查看 SQL 生成调用树和替换过程。

适用于大数据场景下复杂 SQL 的编写与维护，有效解决长 SQL 手工编写易错、难改的问题。