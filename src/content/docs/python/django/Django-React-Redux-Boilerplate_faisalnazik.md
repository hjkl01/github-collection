
---
title: Django-React-Redux-Boilerplate
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/faisalnazik/Django-React-Redux-Boilerplate?style=social) ](https://github.com/faisalnazik/Django-React-Redux-Boilerplate)
### [faisalnazik Django-React-Redux-Boilerplate](https://github.com/faisalnazik/Django-React-Redux-Boilerplate)

**核心内容总结：**  
该项目是一个集成 Django REST 框架、React 和 Redux 的全栈开发模板，包含以下功能：  

- **后端**：基于 Django REST 框架构建 API，支持 JWT 认证（注册、登录）、数据库操作（Django ORM）、限流策略、Pytest 测试及推荐的 Argon2 密码哈希算法。  
- **前端**：使用 React 函数组件和 Hooks，集成 Redux 状态管理、Formik 表单验证、Prettier 代码格式化，并提供登录示例和服务器错误处理。  

**使用方法**：  
1. **后端**：创建虚拟环境并安装依赖（`pip install -r requirements/local.txt`），运行数据库迁移（`makemigrations` / `migrate`），通过 `pytest` 运行测试，访问 API 文档（`http://localhost:8000/api/v1/schema/redoc/`）和管理后台（`http://localhost:8000/admin/`）。  
2. **前端**：安装 Node.js v18.12.1，进入前端目录执行 `yarn install` 和 `yarn start`，访问 `http://localhost:3000/`。  

**主要特性**：  
- 后端支持 JWT 认证、限流和测试；  
- 前端集成 Redux、Formik 和 Material UI；  
- 项目包含 MIT 许可证，支持 PR，集成 CircleCI 和 CodeClimate 工具。