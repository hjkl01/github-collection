
---
title: vocechat-web
---

### [Privoce vocechat-web](https://github.com/Privoce/vocechat-web)

**项目核心内容总结：**  
VoceChat 是一个基于 Web 的实时语音聊天应用，采用 React + Redux Toolkit 技术栈开发，支持 PWA（渐进式 Web 应用）和 Firebase 通知功能。  

**主要特性：**  
- 使用 TypeScript 和 Redux Toolkit 实现状态管理  
- 支持离线存储（通过 indexDB）和跨平台部署  
- 提供 Docker 镜像用于快速部署服务器  

**使用方法：**  
1. **部署服务器**：通过 Docker 命令一键启动服务（支持 x86_64 平台）。  
2. **本地开发**：克隆代码库后使用 pnpm 安装依赖并启动开发环境（`pnpm start`）。  
3. **测试体验**：可访问官方站点（https://voce.chat）或演示地址（https://privoce.voce.chat/）。  

**技术依赖：**  
- 前端框架：React、Redux Toolkit  
- 编辑器组件：Plate（文本编辑器）、TUI Editor（Markdown 编辑器）  
- 存储方案：localForage（indexDB 封装库）  

**许可证：**  
采用 GPL v3 开源协议。