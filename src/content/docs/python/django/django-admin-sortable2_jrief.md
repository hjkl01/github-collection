
---
title: django-admin-sortable2
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/jrief/django-admin-sortable2?style=social) ](https://github.com/jrief/django-admin-sortable2)
### [jrief django-admin-sortable2](https://github.com/jrief/django-admin-sortable2)

**核心内容总结：**  
该项目为 Django Admin 提供拖放排序功能，支持列表、StackedInline 和 TabularInline 视图。通过 mixin 类实现，无需继承特定基类，可直接集成到现有 `ModelAdmin` 或 `Inline` 类中。  

**主要特性：**  
- 使用 Sortable.JS 替代 jQuery，支持多项目同时拖放；  
- 无需修改模型类，兼容任意继承自 `models.Model` 的模型；  
- 支持多种 Django 版本（兼容性见 PyPI 说明）；  
- 开源 MIT 许可证，提供详细文档和 GitHub 示例。  

**使用方法：**  
在 Admin 类中继承对应 mixin（如 `SortableAdminMixin`），即可启用拖放排序功能，无需额外配置字段或方法。