
---
title: django-guardian
---

### [django-guardian django-guardian](https://github.com/django-guardian/django-guardian)  ![GitHub Repo stars](https://img.shields.io/github/stars/django-guardian/django-guardian?style=social)

django-guardian 是一款 Django 第三方库，用于在 Django 授权后端之上实现对象级权限管理（per-object permissions）。它允许为特定用户或组分配针对特定对象的权限，区别于全局权限。安装后需在设置中注册应用和对象权限认证后端，支持通过 `assign_perm` 函数分配权限，并可在 Django Admin 中使用 `GuardedModelAdmin` 启用对象权限管理，同时支持 django-unfold 集成。