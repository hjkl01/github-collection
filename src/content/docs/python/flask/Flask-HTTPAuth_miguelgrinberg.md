
---
title: Flask-HTTPAuth
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/miguelgrinberg/Flask-HTTPAuth?style=social) ](https://github.com/miguelgrinberg/Flask-HTTPAuth)
### [miguelgrinberg Flask-HTTPAuth](https://github.com/miguelgrinberg/Flask-HTTPAuth)

**Flask-HTTPAuth 核心内容总结：**

**项目功能**  
为 Flask 提供 Basic（基本）、Digest（摘要）和 Token（令牌）三种 HTTP 认证方式，用于保护路由接口。

**使用方法**  
1. **安装**：通过 `pip install Flask-HTTPAuth` 安装。  
2. **基本认证**：  
   - 使用 `HTTPBasicAuth` 类，结合 `verify_password` 回调验证用户名和密码（支持密码哈希）。  
   - 示例：定义用户字典，通过 `generate_password_hash` 和 `check_password_hash` 处理密码。  
3. **摘要认证**：  
   - 使用 `HTTPDigestAuth` 类，需设置 `SECRET_KEY`，通过 `get_password` 回调返回用户密码。  

**主要特性**  
- 支持多种认证方式（Basic/Digest/Token）。  
- 提供密码哈希生成与验证功能（依赖 Werkzeug）。  
- 可自定义验证逻辑（如 `verify_password` 和 `get_password` 回调）。  
- 文档详细，支持复杂场景（如 Token 认证）。