
---
title: shannon
---

### [KeygraphHQ shannon](https://github.com/KeygraphHQ/shannon)  ![GitHub Repo stars](https://img.shields.io/github/stars/KeygraphHQ/shannon?style=social)

Shannon 是由 Keygraph 开发的自主式白盒 AI 渗透测试工具，专门用于 Web 应用及 API 的安全测试。它通过结合源代码分析与实时漏洞利用，自动识别攻击向量并生成包含可复现概念验证（PoC）的有效漏洞报告。

**核心功能：**
1. **全自动化操作**：自动处理登录（含 2FA/SSO）、浏览器导航、漏洞利用执行及报告生成。
2. **代码感知动态测试**：基于源代码分析指导攻击策略，通过浏览器自动化和命令行工具对运行中的应用进行验证。
3. **OWASP 漏洞覆盖**：支持注入、XSS、SSRF、认证与授权漏洞的检测，采用并行处理提升效率。
4. **多模型支持**：兼容 Anthropic、AWS Bedrock、Google Vertex AI 等多种 AI 服务。

**产品版本：**
提供 Shannon Lite（开源 AGPL 协议，仅白盒测试）和 Shannon Pro（商业版，含 SAST/SCA 等全栈安全能力）。

**使用限制：**
基于 CLI 运行，需 Docker 环境。**严禁在生产环境使用**，仅限测试、沙箱或开发环境，利用过程可能导致目标应用数据修改。