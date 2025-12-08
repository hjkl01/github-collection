
---
title: kms-tools
---

### [ikxin kms-tools](https://github.com/ikxin/kms-tools)

**项目核心内容总结：**

**功能**  
一站式 KMS 工具箱，集成 KMS 激活脚本生成、服务器检测、状态监控等功能。

**使用方法**  
- **全栈版本**：需部署后端服务，支持 Docker 部署或手动构建（依赖 Node.js 的 `child_process` 模块调用 `vlmcs` 工具）。  
- **静态版本**：可托管于 Vercel、Cloudflare Pages 等平台，通过环境变量 `NUXT_PUBLIC_API_URL` 指定 API 接口地址，部分平台需设置 `NODE_VERSION=22`。

**主要特性**  
- 支持全栈（含后端服务）与静态版本（仅前端）部署模式。  
- 技术栈包含 Nuxt、Vue.js、Tailwind CSS 等，采用现代化开发工具（Vite、Nitro）。  
- 提供 KMS 服务器监控自定义配置（如 `MONITOR_LIST` 环境变量）。