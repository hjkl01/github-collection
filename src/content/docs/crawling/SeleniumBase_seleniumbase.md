
---
title: SeleniumBase
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/seleniumbase/SeleniumBase?style=social) ](https://github.com/seleniumbase/SeleniumBase)
### [seleniumbase SeleniumBase](https://github.com/seleniumbase/SeleniumBase)

**SeleniumBase 核心内容总结：**

**项目功能**  
SeleniumBase 是一个基于 Python 的自动化测试框架，扩展了 Selenium WebDriver 的功能，提供更简洁的 API 和丰富的测试工具，用于 Web 应用的端到端测试。支持多浏览器（Chrome、Firefox、Edge 等）、多平台（Windows、macOS、Linux）及移动端测试。

**使用方法**  
1. **安装**：通过 `pip install seleniumbase` 安装。  
2. **编写测试**：继承 `BaseCase` 类，使用内置方法（如 `open()`、`click()`、`assert_text()` 等）编写测试用例。  
3. **运行测试**：通过 `pytest` 执行测试，支持参数化测试、并行执行及生成 HTML 测试报告。  
4. **高级功能**：支持延迟断言（`deferred_assert`）、测试数据管理、浏览器截图自动保存、日志记录等。

**主要特性**  
- **简化 API**：提供封装好的方法，减少代码冗余（如自动等待元素、智能定位器）。  
- **断言工具**：内置多种断言方法（元素存在性、文本匹配、表单验证等）。  
- **测试增强**：支持测试重试、失败截图、延迟断言汇总错误、与 CI/CD 工具集成。  
- **跨平台兼容**：适配主流浏览器及操作系统，支持移动端测试。  
- **社区支持**：提供详细文档、GitHub 仓库、Discord 社区及中文/英文教程资源。  

**适用场景**  
适用于 Web 应用的功能测试、回归测试、UI 自动化及持续集成环境中的自动化测试需求。