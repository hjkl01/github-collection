
---
title: naxsi
---

### [nbs-system naxsi](https://github.com/nbs-system/naxsi)

Naxsi 是 Nginx 的第三方模块，用于防御 XSS 和 SQL 注入攻击。其核心功能是通过预设规则（如过滤 `<`、`|`、`drop` 等字符）拦截恶意请求，默认采用“拒绝所有、白名单放行”的策略。使用时需管理员手动添加白名单规则，或通过自动学习网站行为生成规则。主要特性包括：基于规则匹配而非签名检测、开源免费、兼容主流 UNIX 系统及多版本 Nginx。