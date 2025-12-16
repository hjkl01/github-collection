
---
title: darkwire.io
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/darkwire/darkwire.io?style=social) ](https://github.com/darkwire/darkwire.io)
### [darkwire darkwire.io](https://github.com/darkwire/darkwire.io)

**核心内容总结：**  
Darkwire.io 是一个基于 Web 的加密聊天应用，使用 RSA-OAEP、AES-CBC 和 HMAC 实现端到端加密，支持群聊和文件传输（最大 4MB）。  

**功能与特性：**  
- **加密通信**：消息和文件通过客户端加密传输，服务器仅存储公钥，不保存聊天记录。  
- **群聊支持**：通过加密会话密钥分发，实现多人聊天。  
- **文件传输**：文件以 Base64 编码后加密传输，支持自定义文件大小限制。  

**使用方法：**  
- **开发环境**：需 HTTPS 连接，通过 `yarn setup` 和 `yarn dev` 启动服务，或使用 `docker-compose up` 自动配置。  
- **生产部署**：执行 `yarn build` 构建项目，通过 `yarn start` 或 Docker 部署。  

**注意事项：**  
- 无服务器端身份验证，需依赖未来可能增加的认证功能。  
- 环境变量需通过 `.env` 文件配置，如 `REACT_APP_MAX_FILE_SIZE` 调整文件限制。