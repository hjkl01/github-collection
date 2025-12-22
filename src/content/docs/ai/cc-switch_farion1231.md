
---
title: cc-switch
---

### [farion1231 cc-switch](https://github.com/farion1231/cc-switch)  ![GitHub Repo stars](https://img.shields.io/github/stars/farion1231/cc-switch?style=social)

**项目核心内容总结：**

1. **项目功能**  
   CC-Switch 是一款跨平台（Windows/macOS/Linux）工具，用于管理和切换多个AI API服务（如Anthropic Claude、OpenAI Codex、Google Gemini）的配置。支持API密钥管理、多账户切换、MCP服务器配置、性能测试（API延迟测量）、云同步（Dropbox/OneDrive等）及自动备份。

2. **使用方法**  
   - 安装方式：通过Cargo、Homebrew或GitHub发布页面下载。  
   - 配置：导入现有Claude/Codex配置，设置云同步目录，重启应用生效。  
   - 操作：通过图形界面或命令行切换API提供商、管理MCP服务器、导出/导入配置、执行性能测试。

3. **主要特性**  
   - **多平台支持**：兼容Windows、macOS、Linux。  
   - **统一数据管理**：采用SQLite数据库（`cc-switch.db`）存储提供商、MCP、提示词等核心数据，JSON文件存储设备级设置。  
   - **云同步**：支持跨设备同步配置，自动轮转备份（保留10份）。  
   - **性能优化**：原子写入防止配置损坏，Mutex锁避免并发冲突，分层架构（前端React+TS/后端Tauri+Rust）提升稳定性。  
   - **开发友好**：100%测试覆盖率（Vitest+MSW）、模块化设计（命令-服务-模型分层）、支持中文/英文双语切换。