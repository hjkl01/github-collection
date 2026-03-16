### [yanglbme geetest-crack](https://github.com/yanglbme/geetest-crack)  ![GitHub Repo stars](https://img.shields.io/github/stars/yanglbme/geetest-crack?style=social)

本项目是一个极验（Geetest）滑动验证码破解工具。其核心功能是不依赖 Selenium 等浏览器自动化操作，而是通过逆向前端 JavaScript 代码，直接解密请求参数并发送 HTTP 请求以通过验证。

主要实现流程包括：
1. 请求参数分析：识别登录请求中的加密参数（如 challenge、validate）。
2. 代码反混淆与提取：还原混淆的 JavaScript 逻辑，封装为 Python 函数用于生成加密数据。
3. 图像与轨迹处理：计算验证码缺口偏移，基于人工滑动轨迹库模拟真实拖动行为。
4. Session 池优化：利用 Redis 预生成有效会话并管理过期，提高登录效率与成功率。

运行需配置 Python 环境、Node.js 及 Redis。项目仅供学习交流使用。