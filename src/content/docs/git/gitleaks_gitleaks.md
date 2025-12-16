
---
title: gitleaks
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/gitleaks/gitleaks?style=social) ](https://github.com/gitleaks/gitleaks)
### [gitleaks gitleaks](https://github.com/gitleaks/gitleaks)

**项目核心内容总结：**

Gitleaks 是一个用于检测代码库中敏感信息（如 API 密钥、密码等）的工具，支持 Git 和目录扫描。其主要功能包括：

- **敏感信息检测**：通过正则表达式、编码解码、归档文件扫描等方式，识别代码中的秘密信息。
- **支持多种扫描方式**：包括 Git 历史记录扫描和目录扫描，支持递归扫描压缩包（如 zip、tar.gz）。
- **自定义规则**：用户可通过配置文件定义检测规则，支持使用正则表达式、忽略特定文件、设置白名单等。
- **支持多种报告格式**：包括 JSON、CSV、Junit、SARIF 等，也支持自定义模板生成报告。
- **忽略特定信息**：可通过 `.gitleaksignore` 文件或代码注释 `gitleaks:allow` 忽略特定秘密信息。
- **解码支持**：支持自动解码百分比、十六进制、Base64 编码的文本，提高检测精度。
- **扩展功能**：支持自定义报告模板，通过 Go 模板语言生成特定格式的输出。
- **退出码控制**：支持自定义检测到秘密信息后的退出码，便于集成到 CI/CD 流程中。

**使用方法**：
- 安装 Gitleaks 后，使用 `gitleaks` 命令进行扫描，如 `gitleaks dir <目录路径>` 或 `gitleaks git <仓库路径>`。
- 可通过 `--report-format` 指定报告格式，使用 `--report-path` 设置报告输出路径。
- 使用 `--max-decode-depth` 和 `--max-archive-depth` 控制解码和归档扫描的深度。

**主要特性**：
- 高度可定制的检测规则；
- 支持多种编码和压缩格式的自动解码与扫描；
- 提供丰富的报告格式和自定义模板；
- 支持忽略特定秘密或文件；
- 集成到 CI/CD 流程中，便于自动化检测。