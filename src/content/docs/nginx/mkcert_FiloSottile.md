
---
title: mkcert
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/FiloSottile/mkcert?style=social) ](https://github.com/FiloSottile/mkcert)
### [FiloSottile mkcert](https://github.com/FiloSottile/mkcert)

mkcert 是一个用于生成本地受信任的开发证书的工具，可自动创建并安装本地证书颁发机构（CA），解决自签名证书的信任问题，适用于开发环境。  

**核心功能**  
- 无需配置，自动生成本地 CA 并安装到系统信任存储（如 macOS、Windows、Linux 的系统证书库及 Firefox）。  
- 支持为域名、IP 地址、本地主机等生成证书，如 `mkcert example.com localhost`。  
- 生成的证书包含 `.pem` 格式的证书文件和私钥文件。  

**使用方法**  
1. 安装：通过 Homebrew（macOS/Linux）、包管理器（如 Arch 的 `pacman`）或手动下载二进制文件安装。  
2. 初始化：运行 `mkcert -install` 安装本地 CA。  
3. 生成证书：使用 `mkcert <域名/IP>` 命令生成证书文件。  

**主要特性**  
- 支持多平台（macOS、Linux、Windows）及主流浏览器（Chrome、Firefox）和 Java 环境。  
- 提供高级选项，如生成 ECDSA 密钥、PKCS#12 文件、客户端证书及 S/MIME 证书（当输入为邮箱时自动触发）。  
- 可自定义 CA 存储路径，但需注意：`rootCA-key.pem` 私钥文件需严格保密，不可分享。  

**注意事项**  
- 仅适用于开发环境，不建议用于生产。  
- 移动设备需手动安装 `rootCA.pem` 以信任证书。  
- Node.js 需通过设置 `NODE_EXTRA_CA_CERTS` 环境变量使用证书。