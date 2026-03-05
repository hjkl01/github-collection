
---
title: webdav
---

### [hacdias webdav](https://github.com/hacdias/webdav)  ![GitHub Repo stars](https://img.shields.io/github/stars/hacdias/webdav?style=social)

这是一个使用 Go 语言编写的简单独立 WebDAV 服务器。支持通过二进制、源码、Homebrew 或 Docker 安装。项目允许通过 YAML、JSON 或 TOML 文件进行配置，支持端口设置、TLS 加密、日志管理及 CORS 策略。具备用户认证功能，支持明文或 bcrypt 加密密码，可自定义用户目录及文件权限（增删改查），并提供基于路径或正则表达式的访问规则控制。兼容 Nginx 和 Caddy 反向代理，支持 Systemd 服务配置，并集成 Fail2Ban 机制以防御暴力破解攻击。