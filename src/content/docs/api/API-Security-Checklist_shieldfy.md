
---
title: API-Security-Checklist
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/shieldfy/API-Security-Checklist?style=social) ](https://github.com/shieldfy/API-Security-Checklist)
### [shieldfy API-Security-Checklist](https://github.com/shieldfy/API-Security-Checklist)

该文档是一个**API安全检查清单**，旨在为开发者在设计、测试和发布API时提供全面的安全措施参考。其核心内容涵盖以下关键领域：

1. **认证与授权**  
   - 推荐使用标准认证方式（如JWT），避免使用Basic Auth。  
   - 对于OAuth，需严格验证`redirect_uri`，防止CSRF攻击，并强制使用代码交换（禁用`response_type=token`）。  

2. **访问控制**  
   - 启用HTTPS（TLS 1.2+）和HSTS头，防止中间人攻击和SSL剥离攻击。  
   - 通过速率限制（如限制请求次数）防御DDoS攻击。  
   - 对私有API限制访问源IP或主机。  

3. **输入验证**  
   - 使用HTTP方法（GET/POST/PUT/DELETE）与业务逻辑匹配，返回`405 Method Not Allowed`错误。  
   - 验证`Content-Type`及数据格式，防止XSS、SQL注入等攻击。  
   - 禁止在URL中暴露敏感信息（如密码、API密钥），改用`Authorization`头。  

4. **数据处理安全**  
   - 避免使用自动递增ID，改用UUID确保唯一性与隐私。  
   - 禁用XML实体解析（防止XXE攻击），并限制数据大小。  
   - 使用CDN处理文件上传，后台处理大数据时启用Workers/Queues。  

5. **输出安全**  
   - 添加安全头信息（如`X-Content-Type-Options: nosniff`、`X-Frame-Options: DENY`、`Content-Security-Policy`）防御XSS、MIME嗅探和点击劫持。  
   - 强制HTTPS，禁止跨域策略（`X-Permitted-Cross-Domain-Policies: none`）。  

6. **CI/CD与依赖安全**  
   - 在CI/CD流程中集成静态代码分析（如SonarQube）、动态测试（如OWASP ZAP）和依赖项漏洞扫描（如Snyk）。  
   - 部署前进行安全审计。  

7. **监控与日志**  
   - 实时监控异常活动，记录请求/响应日志（IP、时间戳、用户代理等）。  
   - 使用日志分析工具检测攻击行为，并设置警报机制。  

8. **工具推荐**  
   - 推荐使用OWASP ZAP、SonarQube、Snyk等工具进行渗透测试、代码审计和依赖扫描。  

9. **社区贡献**  
   - 项目接受社区提交Pull Request，鼓励协作完善安全实践。  

**总结**：该清单为开发者提供了一套系统化的API安全检查框架，覆盖从认证到监控的全生命周期，结合技术实践与工具推荐，帮助构建更安全的API服务。