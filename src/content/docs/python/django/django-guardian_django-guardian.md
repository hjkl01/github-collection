
---
title: django-guardian
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/django-guardian/django-guardian?style=social) ](https://github.com/django-guardian/django-guardian)
### [django-guardian django-guardian](https://github.com/django-guardian/django-guardian)

**核心内容总结：**  
`django-guardian` 是 Django 的一个扩展库，用于实现 **基于对象的权限控制**，允许对 Django 模型的单个实例（而非全局）设置细粒度权限。  

**主要功能：**  
- 支持通过 `assign_perm` 为用户或组分配针对特定对象的权限。  
- 与 Django Admin 集成，通过继承 `GuardedModelAdmin` 实现对象权限管理界面。  
- 支持与第三方工具（如 `django-unfold`）的兼容性。  

**使用方法：**  
1. 安装：通过 `pip install django-guardian` 或包管理工具（如 `uv`/`poetry`）安装。  
2. 配置：将 `guardian` 添加到 `INSTALLED_APPS`，并在 `AUTHENTICATION_BACKENDS` 中注册 `ObjectPermissionBackend`，然后运行 `migrate` 创建数据库表。  
3. 使用：通过 `assign_perm` 为用户分配对象权限，例如 `assign_perm('change_group', user, obj=group)`。  

**主要特性：**  
- 提供高覆盖率（97.6%）的单元测试。  
- 支持 Django 多个版本（Python 3.x）。  
- 文档完善，包含实际项目使用案例。