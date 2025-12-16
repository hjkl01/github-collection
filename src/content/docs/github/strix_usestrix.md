
---
title: strix
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/usestrix/strix?style=social) ](https://github.com/usestrix/strix)
### [usestrix strix](https://github.com/usestrix/strix)

**项目核心内容总结：**

**Strix** 是一个开源的 AI 安全工具，通过动态运行代码、模拟黑客攻击行为，自动检测并验证应用程序中的安全漏洞，提供真实可操作的修复建议，适用于开发团队和安全团队快速进行安全测试。

**主要功能：**
- 动态代码分析与漏洞验证（如注入攻击、访问控制、XSS 等）
- 集成 GitHub Actions 和 CI/CD 流程，实现自动化漏洞扫描
- 支持本地或云端运行（云版本无需配置，直接通过 [app.usestrix.com](https://usestrix.com) 使用）

**使用方法：**
1. 安装：`pipx install strix-agent`
2. 配置 LLM 密钥（如 OpenAI、Anthropic 等）
3. 执行扫描：
   - 本地代码：`strix --target ./app-directory`
   - 在线应用：`strix --target https://your-app.com`
   - GitHub 仓库：`strix --target https://github.com/org/repo`
4. 云端版本可直接通过网页使用，无需安装

**主要特性：**
- **AI 代理工具**：集成 HTTP 代理、浏览器自动化、终端环境、Python 运行时等安全测试工具
- **全面漏洞检测**：覆盖访问控制、注入攻击、业务逻辑漏洞等 20+ 类型
- **多代理协作**：分布式工作流、并行测试、动态协调
- **CI/CD 集成**：GitHub Actions 自动化扫描，阻止漏洞代码合并
- **报告与修复**：生成可操作的修复建议，支持团队协作跟踪

**注意事项：**
- 仅用于合法授权的应用测试，避免非法使用。