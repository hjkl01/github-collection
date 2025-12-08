
---
title: lldap
---

### [lldap lldap](https://github.com/lldap/lldap)

**项目核心内容总结：**

**功能**  
LLDAP 是一个轻量级 LDAP 认证服务器，提供简化用户管理功能，支持通过 Web 界面创建/管理用户、组及属性，用户可自助修改信息或重置密码。它不提供完整 LDAP 服务，而是作为外部认证源，兼容 Nextcloud、Authelia、KeyCloak 等服务，支持 SQLite、MySQL、PostgreSQL 等数据库后端。

**使用方法**  
- 安装方式：Docker/Podman、Kubernetes、包管理器（如 Archlinux/Debian/Ubuntu 等）或从源码编译。  
- 管理方式：通过 Web 界面操作，或使用 CLI 工具（如 `lldap-cli`）及 GraphQL API 脚本化管理。  
- 推荐架构：反向代理（如 Nginx）+ 认证服务（如 Authelia）+ LLDAP 服务，LDAP 端口仅对容器内部开放，支持 LDAPS 加密通信。

**主要特性**  
- 简单易用：无需配置复杂 LDAP 服务，提供默认配置降低使用门槛。  
- 资源占用低：适合自托管场景。  
- 兼容性：支持主流 LDAP 客户端，提供示例配置文件（如与 Nextcloud 集成）。  
- 安全性：默认使用 SQLite 存储数据，支持密码零知识证明方案，限制管理员权限（如 `lldap_admin` 组）。  

**限制**  
- 不支持 LDAP 浏览工具及 Synology 等需密码哈希验证的服务。  
- 需自行配置 SMTP 邮件服务以实现密码重置功能。