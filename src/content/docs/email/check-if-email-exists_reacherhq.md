
---
title: check-if-email-exists
---

### [reacherhq check-if-email-exists](https://github.com/reacherhq/check-if-email-exists)  ![GitHub Repo stars](https://img.shields.io/github/stars/reacherhq/check-if-email-exists?style=social)

这是一个开源工具，用于在不发送邮件的情况下验证电子邮件地址是否存在及有效性。

核心功能：
1. **多方式部署**：支持 HTTP 后端（Docker）、命令行工具（CLI）及 Rust 库编程集成。
2. **全面验证**：检测邮箱语法、DNS MX 记录、可达性（安全/风险/无效）、SMTP 连接与投递状态、邮箱状态（禁用/满/全收）、一次性或角色邮箱识别、Gravatar 信息及数据泄露记录。
3. **标准输出**：返回包含详细验证字段的 JSON 格式数据。