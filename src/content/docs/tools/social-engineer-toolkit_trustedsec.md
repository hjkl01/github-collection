
---
title: social-engineer-toolkit
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/trustedsec/social-engineer-toolkit?style=social) ](https://github.com/trustedsec/social-engineer-toolkit)
### [trustedsec social-engineer-toolkit](https://github.com/trustedsec/social-engineer-toolkit)

**项目核心内容总结：**  
Social-Engineer Toolkit (SET) 是一个开源渗透测试框架，专为社会工程攻击设计，提供多种自定义攻击向量，可快速构建可信攻击场景。由 TrustedSec 开发，支持 Linux 和 Mac OS X（实验性）。  

**使用方法：**  
- **Linux**：克隆仓库后安装依赖（`pip3 install -r requirements.txt`），运行 `python setup.py`。  
- **Mac OS X（M2芯片）**：需创建虚拟环境并激活后安装依赖，再以管理员权限运行 `setup.py`。  
- **Windows 10 WSL/WSL2 Kali Linux**：直接通过 `sudo apt install set -y` 安装。  

**主要特性：**  
- 提供多种社会工程攻击模板，便于快速实施测试；  
- 支持多平台（Linux、Mac、WSL/Kali）；  
- 包含用户手册（PDF格式）及 GitHub 问题跟踪（用于提交 Bug 或功能建议）；  
- 强调仅限合法授权场景使用（如渗透测试），禁止非法用途。