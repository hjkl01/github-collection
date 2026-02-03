
---
title: ansible-collection-hardening
---

### [dev-sec ansible-collection-hardening](https://github.com/dev-sec/ansible-collection-hardening)  ![GitHub Repo stars](https://img.shields.io/github/stars/dev-sec/ansible-collection-hardening?style=social)

**核心内容总结：**  
该项目是一个Ansible集合，提供针对Linux系统（包括CentOS、Debian、Ubuntu等）、MySQL、Nginx和OpenSSH的加固配置，符合Inspec DevSec基线标准。  

**主要功能：**  
- 支持多种Linux发行版（如CentOS、Rocky Linux、Debian、Ubuntu等）及特定版本的MySQL、Nginx和OpenSSH的加固。  
- 部分角色（如Apache和Windows加固）仍在开发中。  

**使用方法：**  
通过`ansible-galaxy collection install devsec.hardening`安装集合，具体使用方式参考各角色的README文档。  

**特性：**  
- 符合DevSec基线合规性要求。  
- 最低要求Ansible 2.16版本。  
- 部分角色支持自定义测试和VM环境验证。  
- 采用Apache 2.0许可证开源。