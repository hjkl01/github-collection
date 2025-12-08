
---
title: django-filter
---

### [carltongibson django-filter](https://github.com/carltongibson/django-filter)

**核心内容总结：**

Django Filter 是一个 Django 应用，用于通过 URL 参数动态过滤查询集（QuerySet），功能类似 Django 管理界面的 `list_filter`，并提供类似 `ModelForm` 的 API。主要特性包括：

1. **功能**  
   - 通过声明式定义过滤条件，实现动态查询数据。  
   - 支持与 Django REST Framework 集成，提供专门的 `FilterSet` 和过滤后端。  

2. **使用方法**  
   - 安装：`pip install django-filter`，并添加 `'django_filters'` 到 `INSTALLED_APPS`。  
   - 定义 `FilterSet` 类（如 `ProductFilter`），指定模型和过滤字段。  
   - 在视图中通过 `request.GET` 传递参数，结合 `FilterSet` 过滤查询集。  
   - 与 DRF 集成时需导入 `django_filters.rest_framework.FilterSet`。  

3. **版本策略**  
   - 使用 `年.版本号`（如 `21.1`）的版本号规则。  
   - 支持当前 Django、Python 及 DRF 最新版本，旧版本在生命周期结束后停止支持。  
   - 重大变更会提前两年弃用（如 `23.x` 引入的特性在 `25.1` 移除）。