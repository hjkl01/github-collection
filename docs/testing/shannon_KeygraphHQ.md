### [KeygraphHQ shannon](https://github.com/KeygraphHQ/shannon)  ![GitHub Repo stars](https://img.shields.io/github/stars/KeygraphHQ/shannon?style=social)

Shannon 是由 Keygraph 开发的自主式 AI 白盒渗透测试工具，旨在通过结合源代码分析与动态利用来发现 Web 应用和 API 的漏洞。

主要功能：
1. **自动渗透测试**：全自动完成侦察、漏洞分析、利用及报告生成，支持多因素认证和浏览器自动化。
2. **代码感知**：基于源码分析指导攻击策略，结合真实运行环境进行验证，覆盖注入、XSS、SSRF 及认证授权问题。
3. **可验证结果**：仅报告可复现的漏洞并提供概念验证（PoC），确保零误报。
4. **多模型支持**：兼容 Anthropic、AWS Bedrock、Google Vertex AI 等主流 AI 模型，支持 Docker 容器化部署。

产品分为开源版（Shannon Lite，用于本地白盒测试）和商业版（Shannon Pro，集成 SAST/SCA 的全栈平台）。仅限拥有源码的应用测试，严禁在生产环境使用，且使用前必须获得明确授权。