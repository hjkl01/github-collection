
---
title: k6-studio
---

### [grafana k6-studio](https://github.com/grafana/k6-studio)  ![GitHub Repo stars](https://img.shields.io/github/stars/grafana/k6-studio?style=social)

Grafana k6 Studio 是一款跨平台（Mac、Windows、Linux）桌面应用，旨在帮助用户生成 k6 性能测试脚本。其核心功能包含三部分：

1.  **Recorder（录制器）**：在浏览器中录制用户操作流程，通过代理捕获请求并生成 HAR 文件。
2.  **Generator（生成器）**：基于 HAR 记录自动创建 k6 测试脚本，无需编写 JavaScript，支持自定义规则（如变量关联）、测试配置及脚本预览导出。
3.  **Validator（验证器）**：执行脚本测试，提供详细的请求响应、日志和断言检查，确保脚本逻辑正确。

该工具的录制功能需要预先安装 Google Chrome 或 Chromium 浏览器。