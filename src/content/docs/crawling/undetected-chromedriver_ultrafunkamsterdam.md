
---
title: undetected-chromedriver
---

### [ultrafunkamsterdam undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)  ![GitHub Repo stars](https://img.shields.io/github/stars/ultrafunkamsterdam/undetected-chromedriver?style=social)

undetected_chromedriver 是一个优化的 Selenium ChromeDriver 补丁库，旨在绕过反爬虫服务（如 Distill Network、Imperva、DataDome 等）的检测。

核心功能：
1. 自动下载并修补 Chromedriver 二进制文件，无需手动配置。
2. 兼容当前 Chrome 版本及 Brave 等 Chromium 浏览器，支持无头模式（Headless）。
3. 提供便捷工具函数（如递归查找元素、安全点击、CDP 事件监听）。
4. 自动处理版本兼容性，避免版本不匹配错误。

注意事项：
1. 不隐藏 IP 地址，从数据中心运行可能无法通过验证。
2. 需 Python 3.6+，安装后直接调用 `uc.Chrome()` 即可使用。