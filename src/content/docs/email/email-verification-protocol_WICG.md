
---
title: email-verification-protocol
---

### [WICG email-verification-protocol](https://github.com/WICG/email-verification-protocol)  ![GitHub Repo stars](https://img.shields.io/github/stars/WICG/email-verification-protocol?style=social)

该协议允许 Web 应用在无需发送邮件且用户无需离开页面的情况下获取已验证的邮箱地址。它解决了传统验证流程中的用户流失、交付延迟和隐私泄露问题。核心机制是邮件域通过 DNS 记录将验证权限委托给授权的发行人。浏览器作为中介，利用用户与发行人的认证 Cookie 请求并接收签名令牌（SD-JWT+KB），确保发行人无法获知具体是哪个应用发起请求，从而保护隐私。最终，Web 应用通过验证令牌及 DNS 记录来确认邮箱所有权。