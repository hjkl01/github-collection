
---
title: hyperliquid-python-sdk
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/hyperliquid-dex/hyperliquid-python-sdk?style=social) ](https://github.com/hyperliquid-dex/hyperliquid-python-sdk)
### [hyperliquid-dex hyperliquid-python-sdk](https://github.com/hyperliquid-dex/hyperliquid-python-sdk)

**项目核心内容总结：**  
`hyperliquid-python-sdk` 是一个用于与 Hyperliquid API 进行交易的 Python SDK。主要功能包括：  
- **安装方法**：通过 `pip install hyperliquid-python-sdk` 安装。  
- **配置要求**：需设置 `account_address`（主钱包公钥）和 `secret_key`（API 钱包私钥），配置文件示例见 `examples/config.json`。  
- **使用示例**：通过 `Info` 类获取用户状态，如 `info.user_state("钱包地址")`；完整示例见 `examples` 目录。  

**主要特性**：  
- 支持语义化版本管理（Semantic Versions）。  
- 代码风格遵循 `black`，并集成 `pre-commit` 进行代码格式化和安全检查（如 `bandit`）。  
- 提供开发贡献指南，要求使用 Python 3.10 和 `Poetry` 管理依赖。  
- 依赖项定期更新，支持通过 `Makefile` 命令进行安装、测试、构建等操作。  
- 使用 MIT 许可证开源，项目模板基于 `python-package-template` 生成。  

**注意事项**：  
- 配置时需区分主钱包公钥与 API 钱包私钥。  
- 发布版本需通过 `poetry version` 更新版本号，并使用 `poetry publish` 发布。