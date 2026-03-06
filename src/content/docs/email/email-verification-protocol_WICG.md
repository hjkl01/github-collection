
---
title: email-verification-protocol
---

### [WICG email-verification-protocol](https://github.com/WICG/email-verification-protocol)  ![GitHub Repo stars](https://img.shields.io/github/stars/WICG/email-verification-protocol?style=social)

邮件验证协议（Email Verification Protocol）允许 Web 应用在不发送邮件且用户无需离开当前页面的情况下，获取已验证的电子邮件地址，解决了传统验证方式存在的用户摩擦、投递延迟及隐私泄露问题。

其核心机制是邮件域名通过 DNS TXT 记录将验证权委托给指定的签发者（Issuer）。当用户输入邮箱后，浏览器利用现有的身份验证 Cookie 向签发者请求令牌。签发者验证用户控制权后返回 SD-JWT 格式的颁发令牌，浏览器验证后将其与公钥绑定生成 SD-JWT+KB 令牌并提交给 Web 应用，由应用验证确认邮箱有效性。

该方案通过浏览器中介请求，确保签发者无法获知具体的 Web 应用身份，从而增强了用户隐私保护。