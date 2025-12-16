
---
title: mailpit
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/axllent/mailpit?style=social) ](https://github.com/axllent/mailpit)
### [axllent mailpit](https://github.com/axllent/mailpit)

**项目核心内容总结：**  

**功能**：Mailpit 是一款轻量级邮件测试工具，提供 SMTP 服务器、Web 界面和 API 接口。支持邮件查看（含 HTML 格式、附件预览）、实时通知、SMTP/POP3 配置、邮件内容检查（HTML 兼容性、链接有效性、垃圾邮件检测）、消息标记、SMTP 转发与中继、混沌测试（模拟 SMTP 错误）等功能。  

**主要特性**：  
- 单二进制文件或 Docker 镜像部署，跨平台支持（Windows/Linux/macOS）；  
- Web 界面支持邮件搜索、HTTPS/认证、邮件截图生成；  
- 提供 REST API 用于自动化测试；  
- 支持 SMTP/POP3 协议，可配置 TLS/STARTTLS；  
- 高性能，可处理数万封邮件，自动清理旧邮件；  
- 支持通过 Webhook 接收邮件通知。  

**使用方法**：  
- 安装方式包括 Homebrew（Mac）、Arch Linux AUR、脚本安装、下载二进制文件或 Docker 部署；  
- 默认 SMTP 端口 1025，Web 界面端口 8025；  
- 可通过 `mailpit -h` 查看运行参数，支持配置 sendmail 等邮件客户端指向 SMTP 服务。