
---
title: trufflehog
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/trufflesecurity/trufflehog?style=social) ](https://github.com/trufflesecurity/trufflehog)
### [trufflesecurity trufflehog](https://github.com/trufflesecurity/trufflehog)

TruffleHog 是一款用于检测代码库中敏感信息（如 API 密钥、密码等）的工具，支持多种使用场景。  
**核心功能**：  
1. **敏感信息扫描**：通过正则表达式、JWT 验证、Canary Token 检测等方式，识别代码中的泄露凭证。  
2. **多平台支持**：提供命令行工具、GitHub Action、GitLab CI、pre-commit 钩子等集成方式，支持 HuggingFace、AWS、Google Cloud 等平台的凭证分析。  
3. **自定义检测**：允许用户通过正则表达式定义自定义检测规则，并通过 Webhook 实现验证逻辑。  

**使用方法**：  
- 命令行：扫描本地文件（如 `trufflehog filesystem path`）、GitHub 仓库（如 `trufflehog github`）、S3 存储桶（如 `trufflehog s3 --bucket`）等。  
- GitHub Action：通过 `extra_args` 配置扫描范围和结果输出，支持 PR 和 Push 事件触发。  
- GitLab CI：通过脚本安装并集成到流水线中，扫描指定路径。  
- Pre-commit 钩子：阻止包含敏感信息的代码提交。  

**主要特性**：  
- 支持 HMAC 和公钥加密 JWT 的有效性验证。  
- 提供深度分析功能（`trufflehog analyze`），查看凭证权限和访问资源。  
- 支持多角色 S3 权限扫描，通过 `--role-arn` 指定 IAM 角色。  
- 从 v3.0 开始采用 AGPL 3.0 许可证，保留与 v2 的 CLI 兼容性。  

**注意事项**：  
- 自定义检测功能为实验性（alpha），可能变更。  
- 扫描范围可通过 `--results` 参数过滤（如 `verified,unknown`）。