
---
title: ungit
---

### [FredrikNoren ungit](https://github.com/FredrikNoren/ungit)

**核心内容总结：**  
ungit 是一个基于 Web 的 Git 图形化界面工具，旨在简化 Git 操作，同时保留其功能灵活性。主要特性包括：  
- **跨平台支持**：兼容所有支持 Node.js 和 Git 的系统。  
- **Web 访问**：可通过浏览器远程访问（如 http://your-machine:8448）。  
- **集成支持**：与 GitHub、Gerrit（通过插件）无缝协作。  
- **直观 UI**：提供清晰的界面帮助用户理解 Git 操作。  
- **配置灵活**：支持配置文件（如 `~/.ungitrc`）和命令行参数（如 `--port=8080`）。  

**使用方法**：  
1. 安装依赖：Node.js（≥20.19.0）、npm（≥10.8.2）、Git（≥2.34.x）。  
2. 全局安装：`npm install -g ungit`（需 root 权限时使用 `sudo -H`）。  
3. 启动：在任意目录运行 `ungit`，浏览器将自动打开界面。  

**其他特性**：  
- 支持 PGP 签名（需 Git 配置或 `.ungitrc` 设置）。  
- 可自定义外部合并工具（如 Kaleidoscope）。  
- 自动刷新文件变更（需非 `.gitignore` 文件）。  
- 提供 Atom、Brackets、VSCode 插件集成。  

**注意事项**：  
- 安装时需确保 Node.js、npm、Git 版本符合要求。  
- Mac 用户若遇崩溃，需更新 npm 和 Node.js。  
- Ubuntu/Debian 用户可能需手动安装新版 Git/Node.js。  
- 部分广告拦截工具可能阻止 Ungit，需添加白名单。  
- 非英文环境运行 Git 可能导致解析错误。