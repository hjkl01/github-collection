
---
title: Telegram-iOS
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/TelegramMessenger/Telegram-iOS?style=social) ](https://github.com/TelegramMessenger/Telegram-iOS)
### [TelegramMessenger Telegram-iOS](https://github.com/TelegramMessenger/Telegram-iOS)

**Telegram iOS源码编译指南核心内容总结**  

**项目功能**  
提供Telegram iOS客户端的源码编译方法，帮助开发者基于Telegram API和源码构建自定义应用。  

**使用方法**  
1. **获取代码**：通过`git clone`命令下载源码。  
2. **配置环境**：安装Xcode，生成随机标识符并配置Xcode项目参数（如组织标识、Team ID）。  
3. **生成项目**：使用Python脚本（`Make.py`）生成Xcode项目，需指定配置文件路径和代码签名信息。  
4. **构建IPA**：通过指定发布证书和配置文件，使用`Make.py`脚本生成发布版本。  

**主要特性**  
- 开发者需自行申请`api_id`，并禁止使用Telegram官方名称和Logo。  
- 支持模拟器构建（无需代码签名），可通过参数`--disableProvisioningProfiles`跳过。  
- 版本兼容性检查：编译前会验证Xcode版本是否符合`versions.json`要求，可强制绕过检查。  
- 高级配置：提供App Store发布所需的证书、配置文件模板及构建参数。