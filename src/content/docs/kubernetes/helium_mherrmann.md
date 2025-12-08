
---
title: helium
---

### [mherrmann helium](https://github.com/mherrmann/helium)

**项目核心内容总结：**

Helium 是一个基于 Python 的浏览器自动化工具，支持 Chrome 和 Firefox，通过高级 API 简化 Web 自动化操作。其核心功能包括：

1. **功能特性**  
   - 无需使用 HTML ID、XPath 或 CSS 选择器，直接通过用户可见标签定位元素，脚本长度比 Selenium 短 30%-50%。  
   - 支持处理嵌套 iFrame、自动管理窗口（如弹窗、标题切换）和隐式/显式等待（如 `wait_until`）。  
   - 与 Selenium 兼容，可混合使用，保留 Selenium 的底层能力。

2. **使用方法**  
   - 安装 Python 3 和浏览器，创建虚拟环境后通过 `pip install helium` 安装。  
   - 示例代码：`from helium import *` 后直接调用相关函数。

3. **项目状态**  
   - 作者因时间限制主要接受 Pull Request 贡献，但提供文档和测试支持。  
   - 可通过 GitHub 星标、社交分享等方式推广项目。