
---
title: webdav
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/hacdias/webdav?style=social) ](https://github.com/hacdias/webdav)
### [hacdias webdav](https://github.com/hacdias/webdav)

**项目核心内容总结：**  

**功能**  
webdav 是一个基于 Go 语言的简单独立 WebDAV 服务器，支持文件管理、用户权限控制、TLS 加密、CORS 配置等功能，适用于搭建文件共享和访问服务。  

**使用方法**  
1. **安装**：支持手动下载二进制文件、Homebrew 安装（`brew install webdav`）、或通过 Go 工具链构建（`go install`）。  
2. **Docker 使用**：需提供配置文件并挂载数据目录，示例命令：  
   ```bash
   docker run -p 6060:6060 -v $(pwd)/config.yml:/config.yml:ro -v $(pwd)/data:/data hacdias/webdav -c /config.yml
   ```  
3. **配置**：通过 YAML/JSON/TOML 文件设置端口、目录、TLS 证书、用户权限、CORS 规则等。  

**主要特性**  
- **权限管理**：支持用户权限（读/写/删除等）和路径级规则配置（如限制特定目录访问）。  
- **反向代理支持**：提供 Nginx/Caddy 配置示例，解决 502 错误问题。  
- **安全增强**：集成 Fail2Ban 防 brute-force 攻击，支持日志分析和 IP 封禁。  
- **灵活配置**：支持 TLS、CORS、日志格式（JSON/控制台）、环境变量用户认证等。  

**注意事项**  
- 反向代理需正确设置 `X-Forwarded-For` 等头信息。  
- 用户配置支持 bcrypt 密码加密和环境变量注入。