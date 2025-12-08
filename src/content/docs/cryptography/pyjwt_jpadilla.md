
---
title: pyjwt
---

### [jpadilla pyjwt](https://github.com/jpadilla/pyjwt)

PyJWT 是一个 Python 库，用于实现 JSON Web Token (JWT) 标准（RFC 7519），支持生成和验证 JWT 令牌。  

**使用方法**：通过 pip 安装（`pip install PyJWT`），使用 `jwt.encode()` 编码数据，用 `jwt.decode()` 解码验证，需指定密钥和算法（如 HS256）。  

**主要特性**：  
- 遵循 JWT 标准，支持常见加密算法（示例中使用 HS256）；  
- 提供详细文档（[在线文档链接](https://pyjwt.readthedocs.io/en/stable/)）；  
- 支持通过 `tox` 运行测试用例，确保代码质量。