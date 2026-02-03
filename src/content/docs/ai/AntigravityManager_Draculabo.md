
---
title: AntigravityManager
---

### [Draculabo AntigravityManager](https://github.com/Draculabo/AntigravityManager)  ![GitHub Repo stars](https://img.shields.io/github/stars/Draculabo/AntigravityManager?style=social)

**项目名称**：Antigravity Manager（反重力管理器）

**项目简介**：  
Antigravity Manager 是一款专为管理 Google Gemini 和 Claude AI 多账号的专业桌面应用，基于 Electron、React 和 TypeScript 开发，提供本地 API 代理、智能切换账号、实时额度监控、安全加密等功能，解决单账号配额不足、账号切换繁琐等问题。

---

**核心功能**：

1. **多账号池管理**  
   - 支持添加无限 Google Gemini / Claude 账号（通过 OAuth 登录）
   - 显示账号头像、邮箱、状态、上次使用时间
   - 实时监控账号状态（活跃 / 限速 / 过期）

2. **智能自动切换**  
   - 当当前账号配额低于 5% 或被限速时，自动切换到下一个可用账号
   - 每 5 分钟后台自动检测一次账号状态

3. **实时配额监控**  
   - 支持多种模型（如 gemini-pro、claude-3-5-sonnet 等）
   - 可视化进度条显示配额使用情况
   - 支持手动和自动刷新

4. **本地 API 代理**  
   - 内置 OpenAI / Anthropic 格式兼容的代理服务
   - 可配置端口、超时时间
   - 支持模型映射（如将 Claude 映射为 Gemini）

5. **安全加密**  
   - 使用 AES-256-GCM 加密敏感数据
   - 集成操作系统原生凭证管理
   - 自动迁移旧版明文数据

6. **系统托盘与 IDE 同步**  
   - 支持后台运行，系统托盘图标控制
   - 自动扫描并导入 Antigravity IDE 的账号信息（state.vscdb）

7. **开发者工具**  
   - 内置 cURL 和 Python 代码生成
   - 可视化服务状态监控
   - 一键生成 API Key

---

**使用方法**：

1. **下载安装**  
   - 支持 Windows、macOS、Linux 平台
   - 从 [GitHub Releases](https://github.com/Draculabo/AntigravityManager/releases) 下载对应安装包

2. **源码构建**  
   - 需要 Node.js v18 或更高版本
   - 克隆仓库后执行：
     ```bash
     npm install
     npm start      # 开发模式
     npm run make   # 构建生产版本
     ```

---

**技术栈**：

- **核心框架**：Electron、React、TypeScript  
- **构建工具**：Vite  
- **样式库**：TailwindCSS、Shadcn UI  
- **状态管理**：TanStack Query、TanStack Router  
- **数据库**：Better-SQLite3  
- **测试工具**：Vitest、Playwright  

---

**主要特性总结**：

| 功能模块             | 描述                                                                 |
|----------------------|----------------------------------------------------------------------|
| 多账号池             | 无限添加并管理 Google 和 Claude 账号                                 |
| 智能切换             | 自动切换账号，避免配额耗尽或限速                                   |
| 配额监控             | 实时查看各账号的配额使用情况                                         |
| 本地 API 代理        | 提供兼容 OpenAI/Anthropic 的 API 服务，支持模型映射                  |
| 安全加密             | 敏感数据 AES-256-GCM 加密，集成系统凭证管理                          |
| 托盘与 IDE 同步      | 支持系统托盘后台运行，自动导入 Antigravity IDE 的账号                 |
| 开发者工具           | 代码生成、服务监控、API Key 生成等功能                               |

---

**许可证**：CC BY-NC-SA 4.0（禁止商业用途）  
**开源贡献**：欢迎提交 Issue 和 PR，详情见 [CONTRIBUTING.md](CONTRIBUTING.md)