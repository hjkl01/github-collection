
---
title: age
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/FiloSottile/age?style=social) ](https://github.com/FiloSottile/age)
### [FiloSottile age](https://github.com/FiloSottile/age)

**核心内容总结：**  
age 是一个简单、现代、安全的文件加密工具及 Go 库，支持通过显式小密钥（无需配置）实现加密，兼容 UNIX 风格的组合性操作。其主要功能包括：  
1. **加密与解密**：支持通过 age 公钥（由 `age-keygen` 生成）或 SSH 公钥（如 `ssh-ed25519`）加密文件，解密时使用对应私钥或密码短语。  
2. **多接收者加密**：可同时指定多个接收者（通过 `-r` 或 `-R` 参数），所有接收者均可解密文件。  
3. **密码短语保护**：加密时可自动生成或手动输入密码短语，解密时需输入相同密码。  
4. **SSH 密钥支持**：兼容 SSH 公钥加密及私钥解密，但加密文件会嵌入 SSH 公钥标签，可能被用于追踪。  
5. **安装方式**：支持主流操作系统（如 Linux、macOS）及包管理器（如 Homebrew、APT），也可从源码构建。  
6. **签名验证**：通过 Sigsum 工具验证发布版本的签名，确保文件完整性。  

**主要特性**：  
- 无配置项，操作简洁；  
- 支持 PEM 编码格式输出（`--armor`）；  
- 身份文件可包含多个密钥，自动识别并使用；  
- 密码保护文件可自动检测并提示输入密码。