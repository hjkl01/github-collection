### [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks) ![GitHub Repo stars](https://img.shields.io/github/stars/pre-commit/pre-commit-hooks?style=social)

`pre-commit-hooks` 是一个为 `pre-commit` 提供的开箱即用钩子集合，用于在提交前自动检查与修复代码和仓库问题。主要功能包括：

- **代码与配置语法校验**：检查 Python AST、JSON/TOML/XML/YAML 语法、合并冲突标记、调试语句等。
- **文件规范与格式修复**：去除行尾空白、统一/检查换行符、补齐文件末尾换行、移除 UTF-8 BOM、格式化 JSON、排序 requirements 与简单 YAML。
- **仓库安全与质量防护**：阻止提交超大文件、检测私钥与 AWS 凭证、禁止新增或任何 submodule、保护主分支禁止直接提交。
- **跨平台与可执行性检查**：检查大小写冲突文件名、非法 Windows 文件名、无效符号链接、可执行文件 shebang 合规性。
- **命名与内容规则**：测试文件命名规则检查、字符串引号修复、文件内容排序等。
- **可配置性强**：多数钩子支持参数定制（如大小限制、分支/正则保护、YAML 多文档、JSON 缩进与键排序策略等）。
- **使用方式**：在 `.pre-commit-config.yaml` 引用仓库与版本即可启用；也可通过 `pip install pre-commit-hooks` 作为独立包使用。