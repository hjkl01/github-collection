
---
title: rogue
---

### [qualifire-dev rogue](https://github.com/qualifire-dev/rogue)  ![GitHub Repo stars](https://img.shields.io/github/stars/qualifire-dev/rogue?style=social)

Rogue 是一款 AI 代理评估与红队测试平台，旨在在攻击者之前对 AI 代理进行压力测试和安全加固。核心功能包括：

1. **自动评估**：测试代理对业务策略和预期行为的合规性，适用于回归测试和行为验证。
2. **红队测试**：模拟对抗性攻击以发现安全漏洞（覆盖 75+ 种漏洞和 12 类安全类别），提供 CVSS 风险评分及 OWASP、NIST 等合规框架报告。

技术特性如下：
- **架构**：支持 TUI、CLI 及服务器模式，兼容 CI/CD 流程和非交互模式。
- **协议**：兼容 A2A、MCP 及 Python 函数调用。
- **报告**：提供实时会话监控及 Markdown、CSV、JSON 等多格式综合报告。
- **安全**：支持基于随机种子的可复现扫描及多种大模型集成。