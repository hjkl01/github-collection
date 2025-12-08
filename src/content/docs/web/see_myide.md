
---
title: see
---

### [myide see](https://github.com/myide/see)

**核心内容总结：**  
See SQL审核平台是一个基于Python/Django和Vue.js开发的SQL审核与管理工具，集成Inception（SQL审核执行）、SQLAdvisor（优化建议）和SOAR（启发式优化）等开源组件，支持多数据库环境管理、SQL语法检测、执行回滚、工单审批流程、用户权限控制及数据报表展示。  

**主要功能：**  
- **数据库管理**：支持多数据中心数据库配置、表结构查询及数据导出。  
- **SQL操作**：提供语法检测、执行、回滚、定时工单及历史记录功能。  
- **优化建议**：结合SQLAdvisor和SOAR输出索引优化与语句改进建议。  
- **审批流程**：支持双人确认流程（提交人→自动审核→经理审批→DBA上线）或简化流程（提交人→自动审核→经理上线）。  
- **权限控制**：基于RBAC模型实现表级/对象级权限管理，区分用户组角色（组员/经理/总监）操作权限。  
- **通知与报表**：支持邮件提醒、DashBoard数据审计可视化。  

**使用方法：**  
- **在线访问**：通过提供的链接（http://oldcat.online:52080/）使用默认账号（武松/宋江，密码均为see）登录。  
- **部署安装**：参考GitHub安装文档（https://github.com/myide/see/blob/master/frontend/src/files/install.md）进行本地部署。  
- **集成对接**：提供自动化API文档，支持与外部系统对接。  

**技术特性：**  
- 前端采用Vue.js 2.9 + iView 2.8，后端基于Django 2.0 + Python 3.6。  
- 支持SSO统一认证登录、自定义SQL关键字拦截及审批流程开关等个性化配置。