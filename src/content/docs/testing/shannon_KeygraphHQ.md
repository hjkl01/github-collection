
---
title: shannon
---

### [KeygraphHQ shannon](https://github.com/KeygraphHQ/shannon)  ![GitHub Repo stars](https://img.shields.io/github/stars/KeygraphHQ/shannon?style=social)

**项目名称**：Shannon（一款全自动的AI渗透测试工具）

---

### **核心功能**

Shannon 是一个**全自动的AI渗透测试器**，专门用于**白盒测试**（需要源代码），其目标是在任何攻击者之前**主动发现并验证Web应用中的安全漏洞**。它不仅能识别潜在问题，还能**执行真实攻击**，如注入攻击、认证绕过等，以验证漏洞的可利用性，并提供**可复现的漏洞证明（PoC）**。

---

### **主要特性**

1. **全自动操作**：只需一条命令即可启动渗透测试，AI会自动处理从登录、导航到生成报告的全过程。
2. **可复现的漏洞报告**：提供带有真实攻击代码的详细报告，减少误报，便于开发人员直接修复。
3. **支持关键OWASP漏洞类型**：包括注入（Injection）、XSS、SSRF、认证/授权缺陷等。
4. **源码感知的动态测试**：结合源码分析与浏览器自动化，实现深度漏洞验证。
5. **集成安全工具**：如 Nmap、Subfinder、WhatWeb、Schemathesis 等，用于深度侦察与测试。
6. **并行处理**：多个漏洞类型并行测试，提升效率。
7. **支持2FA登录**：包括TOTP和Google登录等复杂认证流程。
8. **支持自定义配置**：可以设置认证流程、限制测试范围、指定关注路径等。

---

### **产品版本**

| 版本 | 授权协议 | 适用对象 |
|------|----------|-----------|
| **Shannon Lite** | AGPL-3.0 | 安全团队、独立研究者、测试自有应用 |
| **Shannon Pro** | 商业许可 | 企业用户，需要高级功能、CI/CD集成和专属支持 |

---

### **使用方法**

1. **前提条件**：
   - 安装 Docker
   - 准备 AI API 密钥（推荐使用 Anthropic 的 Claude API）

2. **快速启动**：
   ```bash
   git clone https://github.com/KeygraphHQ/shannon.git
   cd shannon
   # 配置 API 密钥
   ./shannon start URL=https://your-app.com REPO=/path/to/your/repo
   ```

3. **监控进度**：
   - 查看日志：`./shannon logs`
   - 查询进度：`./shannon query ID=xxx`
   - Web界面：`http://localhost:8233`

4. **停止运行**：
   ```bash
   ./shannon stop
   ```

---

### **适用场景**

- 本地开发环境或测试环境下的自动化渗透测试
- 对 OWASP Juice Shop、Checkmarx Capital API、OWASP crAPI 等故意脆弱应用进行测试
- 与 CI/CD 管道集成，实现持续安全测试

---

### **注意事项**

1. **不要在生产环境中运行**：Shannon 会主动执行攻击，可能导致数据修改或删除。
2. **需获得授权**：未经授权的扫描和攻击是非法的。
3. **验证报告内容**：尽管采用“通过攻击验证漏洞”的方法，但最终报告仍需人工复核。
4. **Windows防病毒误报**：部分报告中的攻击代码可能被误判为恶意软件，需添加排除。

---

### **许可证**

Shannon Lite 使用 **AGPL-3.0** 开源协议，适合内部使用和私有修改。如用于 SaaS 或托管服务，需公开源码修改部分。

---

### **联系方式**

- Discord：[https://discord.gg/KAqzSHHpRt](https://discord.gg/KAqzSHHpRt)
- 邮箱：[shannon@keygraph.io](mailto:shannon@keygraph.io)
- Shannon Pro 申请：[在线表单](https://docs.google.com/forms/d/e/1FAIpQLSf-cPZcWjlfBJ3TCT8AaWpf8ztsw3FaHzJE4urr55KdlQs6cQ/viewform?usp=header)