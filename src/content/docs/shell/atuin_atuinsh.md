
---
title: atuin
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/atuinsh/atuin?style=social) ](https://github.com/atuinsh/atuin)
### [atuinsh atuin](https://github.com/atuinsh/atuin)

**项目功能**  
Atuin 用 SQLite 数据库替代传统 shell 历史记录，记录命令的上下文（如退出码、执行时间、工作目录等），并支持**端到端加密**的跨设备同步（可选）。  

**使用方法**  
1. 安装：运行 `curl --proto '=https' --tlsv1.2 -LsSf https://setup.atuin.sh | sh`  
2. 注册账户：`atuin register -u <用户名> -e <邮箱>`  
3. 导入历史：`atuin import auto`  
4. 同步数据：`atuin sync`  
5. 重启 shell 生效。  

**主要特性**  
- 全屏搜索界面（支持 `Ctrl+R`/`↑` 触发）  
- 加密同步至云端或自建服务器  
- 跨终端、会话、设备同步历史  
- 记录命令执行时间、退出码、主机名等元数据  
- 统计分析（如“最常用命令”）  
- 快速跳转历史记录（`Alt+数字键`）  
- 支持 zsh、bash、fish 等主流 shell