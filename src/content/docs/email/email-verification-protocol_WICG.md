
---
title: email-verification-protocol
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/WICG/email-verification-protocol?style=social) ](https://github.com/WICG/email-verification-protocol)
### [WICG email-verification-protocol](https://github.com/WICG/email-verification-protocol)

**核心内容总结：**

**项目功能**  
该方案通过SD-JWT（可选披露JWT）和KB-JWT（密钥绑定JWT）实现电子邮件验证，无需发送验证码。浏览器、发件人（RP）和发行者（Issuer）协同验证用户邮箱的真实性，确保隐私与安全性。

**使用方法**  
1. **浏览器验证**：通过DNS的`_email-verification` TXT记录确认邮箱发行者，生成SD-JWT并绑定用户密钥（KB-JWT）。  
2. **RP验证**：接收SD-JWT+KB后，验证KB-JWT的`nonce`和`sd_hash`，并核对SD-JWT的签名、时间戳及邮箱合法性。  

**主要特性**  
- **隐私保护**：发行者不需知晓RP身份，RP无法得知用户是否登录发行者。  
- **安全机制**：结合SD-JWT的可选披露与KB-JWT的密钥绑定，防止令牌篡改。  
- **无需验证码**：通过JWT签名验证替代传统邮件验证码流程。  
- **扩展性**：支持未来通过Passkey或URL登录验证。