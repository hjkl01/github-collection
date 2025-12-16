
---
title: flask-jwt-extended
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/vimalloc/flask-jwt-extended?style=social) ](https://github.com/vimalloc/flask-jwt-extended)
### [vimalloc flask-jwt-extended](https://github.com/vimalloc/flask-jwt-extended)

**项目核心内容总结：**

**功能**  
Flask-JWT-Extended 是 Flask 的 JWT 扩展库，支持通过 JSON Web Token 保护路由，并提供以下特性：  
- 支持在 JWT 中添加自定义声明  
- 自动加载用户（`current_user`）  
- 验证接收令牌的自定义声明  
- 支持刷新令牌及鲜活性令牌（用于敏感操作）  
- 令牌撤销/阻止功能  
- 支持将令牌存储在 Cookie 中并提供 CSRF 保护  

**使用方法**  
- 文档查看：[在线文档链接](https://flask-jwt-extended.readthedocs.io/en/stable/)  
- 升级指南：[4.0.0 版本变更说明](https://flask-jwt-extended.readthedocs.io/en/stable/v4_upgrade_guide/)  
- 版本更新记录：[GitHub 发布页](https://github.com/vimalloc/flask-jwt-extended/releases)  

**贡献方式**  
- 安装开发依赖并运行代码规范检查：  
  ```bash  
  pip install -r requirements.txt  
  pre-commit install  
  ```  
- 运行所有测试及检查：  
  ```bash  
  tox  
  ```  
- 可选参数运行部分检查（如 Python 版本、类型检查、文档构建等）  
- 本地生成文档：进入 `docs` 目录执行 `make clean && make html && open _build/html/index.html`