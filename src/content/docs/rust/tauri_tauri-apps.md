
---
title: tauri
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/tauri-apps/tauri?style=social) ](https://github.com/tauri-apps/tauri)
### [tauri-apps tauri](https://github.com/tauri-apps/tauri)

**Tauri 核心内容总结：**

**项目功能**  
Tauri 是一个用于构建跨平台桌面应用的框架，支持 Windows、macOS、Linux、iOS 和 Android。前端可使用任何能编译为 HTML/JS/CSS 的框架，后端基于 Rust 构建，通过 API 实现前后端交互。应用通过 WRY 库调用系统原生 WebView（如 WKWebView、WebView2 等）渲染界面，无需启动本地 HTTP 服务器。

**使用方法**  
1. 安装系统依赖（如 Rust、Node.js 等）；  
2. 使用 `npm create tauri-app@latest` 命令快速创建新项目；  
3. 参考官方文档（[tauri.app](https://tauri.app)）完成开发和打包。

**主要特性**  
- 内置打包工具，支持生成 `.app`、`.dmg`、`.deb`、`.exe` 等格式的安装包；  
- 内置自更新功能（仅限桌面端）；  
- 支持系统托盘、原生通知；  
- 提供 GitHub Action 模板简化 CI 流程；  
- 支持 VS Code 插件；  
- 跨平台兼容性：Windows 7+、macOS 10.15+、Linux（需 WebKitGTK 4.0+）、iOS 9+、Android 7+。