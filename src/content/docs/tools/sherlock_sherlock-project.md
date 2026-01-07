
---
title: sherlock
---

### [sherlock-project sherlock](https://github.com/sherlock-project/sherlock)  ![GitHub Repo stars](https://img.shields.io/github/stars/sherlock-project/sherlock?style=social)

Sherlock 是一款通过用户名跨 400+ 社交平台搜索账号的工具。核心功能包括：  
- **功能**：根据输入的用户名，批量搜索各平台是否存在相同账号，并输出结果文件（如 TXT/CSV/XLSX）。  
- **使用方法**：  
  1. 安装方式：支持 `pipx install sherlock-project`、`docker run` 或系统包管理器（部分系统需用 pipx/Docker）。  
  2. 命令示例：`sherlock user1 user2`（多用户搜索），支持 `--tor`（Tor 网络）、`--csv`（导出 CSV）、`--site`（指定平台）等参数。  
- **特性**：  
  - 支持多格式输出（文本、表格）、代理/私密模式；  
  - 可通过 Apify 云平台无安装运行；  
  - 提供 NSFW 网站检查选项。  

注意：部分 Linux 发行版的第三方包可能存在问题，建议使用 pipx 或 Docker 安装。