### [trufflesecurity trufflehog](https://github.com/trufflesecurity/trufflehog)  ![GitHub Repo stars](https://img.shields.io/github/stars/trufflesecurity/trufflehog?style=social)

TruffleHog 是一款强大的凭据发现、分类、验证和分析工具，旨在查找泄露的敏感信息（如 API 密钥、数据库密码、私钥等）。

主要功能：
1. **广泛扫描**：支持 Git、GitHub、GitLab、Docker、S3、GCS、Slack、Confluence 等多种数据源及本地文件系统。
2. **精准分类**：识别并分类超过 800 种密钥类型，并映射到具体身份。
3. **主动验证**：通过 API 测试确认凭据是否有效，消除误报。
4. **深度分析**：对常见泄露凭据进行权限和资源访问情况分析。

支持作为 CLI 工具、Docker 容器、GitHub Action、GitLab CI 及 pre-commit 钩子使用，可无缝集成至开发工作流中进行持续监控。