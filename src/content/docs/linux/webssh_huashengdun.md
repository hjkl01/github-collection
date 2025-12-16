
---
title: webssh
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/huashengdun/webssh?style=social) ](https://github.com/huashengdun/webssh)
### [huashengdun webssh](https://github.com/huashengdun/webssh)

### 核心内容总结

**项目功能**  
WebSSH 是一个基于 Python 的网页 SSH 客户端，允许用户通过浏览器连接 SSH 服务器。支持密码、公钥（含多种加密算法）、双因素认证（TOTP）等多种登录方式，提供全屏终端、窗口调整、自动编码检测等功能，兼容主流浏览器。

**使用方法**  
1. 安装：`pip install webssh`  
2. 启动服务：`wssh`（可自定义监听地址、端口、HTTPS 配置等）  
3. 浏览器访问 `http://127.0.0.1:8888`，填写连接信息提交。  
4. 支持通过 URL 参数传递主机、用户名、密码（需 Base64 编码）、终端样式等信息。  
5. Docker 部署：`docker-compose up`。

**主要特性**  
- 支持密码、公钥（DSA/RSA/ECDSA/Ed25519）、加密密钥、双因素认证。  
- 全屏终端、窗口可调整大小、自动检测 SSH 服务器编码。  
- 支持通过 JavaScript API 直接连接服务器（`wssh.connect()`）。  
- 可自定义字体、背景色、字体颜色、终端类型等。  
- 安全性：默认拒绝未知主机密钥，防止中间人攻击。  
- 部署灵活：支持 Nginx 反向代理、HTTPS、日志管理等。