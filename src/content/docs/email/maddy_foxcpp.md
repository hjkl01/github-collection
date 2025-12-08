
---
title: maddy
---

### [foxcpp maddy](https://github.com/foxcpp/maddy)

**核心内容总结：**  
Maddy Mail Server 是一个可组合的全功能邮件服务器，集成 SMTP 邮件传输（MTA/MX）、IMAP 邮件存储及 DKIM/SPF/DMARC 等安全协议，可替代 Postfix、Dovecot 等多款传统工具，以单一进程实现统一配置和低维护成本。其 IMAP 存储功能尚属测试阶段，稳定性可能不足，需注意若需成熟方案建议使用 Dovecot。项目提供教程和文档，支持通过 IRC 和邮件列表交流。  

**主要特性：**  
- 集成 SMTP 发送/接收、IMAP 存储  
- 实现邮件安全协议（DKIM、SPF、DMARC 等）  
- 用单一进程替代多工具，简化配置  
- IMAP 功能为测试版，稳定性待验证