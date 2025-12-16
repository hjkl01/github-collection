
---
title: nginx-proxy-automation
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/evertramos/nginx-proxy-automation?style=social) ](https://github.com/evertramos/nginx-proxy-automation)
### [evertramos nginx-proxy-automation](https://github.com/evertramos/nginx-proxy-automation)

**项目核心内容总结：**  

**功能**  
该项目通过自动化脚本实现 NGINX 反向代理配置，支持域名绑定、SSL 证书自动申请（基于 Let's Encrypt）及 Docker 容器集成，可简化 Web 服务的反向代理部署流程。  

**使用方法**  
1. 克隆代码库（需包含子模块）：`git clone --recurse-submodules https://github.com/evertramos/nginx-proxy-automation.git proxy`  
2. 执行初始化脚本：`cd proxy/bin && ./fresh-start.sh --yes --skip-docker-image-check -e your_email@domain`（需替换为真实邮箱）  
3. 测试代理：通过 Docker 启动测试容器或运行 `./test.sh your.domain.com`（需确保 DNS 解析正确）。  

**主要特性**  
- 自动化处理 SSL 证书申请与续期  
- 支持 Docker 网络集成与容器化服务代理  
- 提供一键初始化脚本简化部署流程  
- 适配多种云服务器环境（如 AWS、Digital Ocean 等）