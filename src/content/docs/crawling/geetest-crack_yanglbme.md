
---
title: geetest-crack
---

### [yanglbme geetest-crack](https://github.com/yanglbme/geetest-crack)  ![GitHub Repo stars](https://img.shields.io/github/stars/yanglbme/geetest-crack?style=social)

本项目是一款极验（Geetest）滑动验证码破解工具，无需使用 Selenium 或 WebDriver，而是通过直接解密 JavaScript 请求参数来绕过验证。

主要功能如下：

1.  **JS 参数解密**：分析网络请求，对极验混淆的 JavaScript 代码进行反混淆、还原及关键逻辑剥离，使用 PyExecJS 在 Python 中生成合法的加密参数（如 challenge、validate 等）。
2.  **滑块轨迹模拟**：还原验证码图片计算缺口偏移量，结合采集的人类滑动轨迹库模拟拖动过程。
3.  **Session 池优化**：利用 Redis 构建验证码 Session 池，预先滑动获取有效会话并实现自动过期管理，大幅提升登录效率与成功率。

需配置 Python 依赖、Node.js 及 Redis 环境。项目仅供学习交流使用。