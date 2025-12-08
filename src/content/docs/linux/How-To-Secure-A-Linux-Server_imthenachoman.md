
---
title: How-To-Secure-A-Linux-Server
---

### [imthenachoman How-To-Secure-A-Linux-Server](https://github.com/imthenachoman/How-To-Secure-A-Linux-Server)

**项目功能**  
该项目指导用户在Linux服务器上配置邮件发送功能及日志管理，核心包括：  
1. **邮件服务器配置**：使用Exim4通过TLS加密发送邮件，支持本地账户别名映射至外部邮箱，配置UFW放行465端口。  
2. **日志管理**：通过rsyslog将iptables日志分离至独立文件，结合logrotate实现日志轮转，提升日志分析效率。  

**使用方法**  
- **邮件配置**：安装Exim4，修改`/etc/aliases`设置别名，配置TLS参数，更新Exim4配置并重启服务。  
- **日志管理**：编写rsyslog规则定向iptables日志，调整psad配置文件路径，重启rsyslog及psad服务，设置logrotate轮转策略。  

**主要特性**  
- 邮件发送支持TLS加密，保障通信安全。  
- 日志分离与轮转机制，优化日志存储与检索。  
- 提供脚本化操作（如UFW规则、rsyslog配置），简化部署流程。