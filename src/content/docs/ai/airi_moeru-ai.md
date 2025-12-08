
---
title: airi
---

### [moeru-ai airi](https://github.com/moeru-ai/airi)

**项目核心内容总结：**  
AIRI 是一个结合虚拟主播（VTuber）、AI 交互和游戏代理功能的综合平台，支持通过 WebXR 实现沉浸式交互，并集成多种大语言模型（LLM）服务。  

**功能与特性：**  
1. **虚拟主播支持**：基于 VRM 模型和 WebXR 技术，实现虚拟角色的实时交互。  
2. **游戏代理能力**：通过 Factorio 和 Minecraft 的代理模块（如 Factorio RCON API、Mineflayer），实现游戏自动化操作。  
3. **AI 集成**：支持多种 LLM 后端（如通过 xsAI 模块），提供自然语言交互能力。  
4. **模块化架构**：包含数据库驱动（DuckDB）、实时音频处理、UI 组件库等独立模块，便于扩展。  
5. **多平台运行**：提供 Web 界面（StageWeb）和桌面应用（StageTamagotchi），支持浏览器和本地运行。  

**使用方法：**  
- 通过 StageWeb 启动 Web 界面，或使用 StageTamagotchi 运行桌面应用。  
- 配置 LLM 服务（如通过 xsAI 模块）和数据库连接，启动相关代理功能（如游戏控制或语音处理）。  

**技术栈：**  
- 前端：Vue、WebXR、TypeScript；后端：Node.js、Rust；数据库：DuckDB、PostgreSQL。