
---
title: DrissionPage
---

### [g1879 DrissionPage](https://github.com/g1879/DrissionPage)

**DrissionPage 项目核心内容总结：**

**项目功能**  
DrissionPage 是一个基于 Python 的网页自动化工具，支持浏览器控制、数据包收发及两者结合使用，兼具浏览器自动化的便利性和 `requests` 的高效率。内置大量实用功能，适用于网页操作、数据抓取等场景。

**使用方法**  
通过 [官方文档](https://DrissionPage.cn) 获取使用指南，支持 Windows、Linux、Mac 系统，兼容 Python 3.6 及以上版本，适用于 Chromium 内核浏览器（如 Chrome、Edge）及 Electron 应用。

**主要特性**  
1. **自研内核优势**：无需 WebDriver，无需安装浏览器驱动，运行更快；支持跨 iframe 查找元素、多标签页同时操作、浏览器缓存读取、全网页截图及非 `open` 状态 shadow-root 处理。  
2. **人性化设计**：提供极简元素定位语法、内置 lxml 解析引擎（速度提升数级）、自动等待与重试机制、浏览器下载工具、INI 配置文件管理、POM 模式封装（便于测试扩展）。  
3. **高效稳定**：通过优化减少代码量，提升开发效率；支持重复使用已打开的浏览器实例，简化调试流程。