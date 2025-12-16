
---
title: Handy
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/cjpais/Handy?style=social) ](https://github.com/cjpais/Handy)
### [cjpais Handy](https://github.com/cjpais/Handy)

**核心内容总结：**  
Handy 是一款跨平台（Windows/macOS/Linux）的离线语音转文字工具，使用 Tauri 框架（Rust + React/TypeScript）开发，支持通过快捷键启动录音并实时将语音转为文字，直接粘贴到其他应用中，无需联网，保障隐私。  

**主要功能与特性：**  
- **本地处理**：语音识别（Whisper/Parakeet 模型）、语音活动检测（VAD）均在本地完成，数据不上传云端。  
- **模型选择**：支持 Whisper（多种版本）及 Parakeet V3（CPU 优化，自动语言识别）。  
- **隐私与开源**：完全免费、开源，代码可扩展，无付费限制。  
- **操作便捷**：通过快捷键或“按住说话”模式触发，转录后自动粘贴至当前应用。  

**使用方法：**  
1. 从官网或 GitHub 下载安装包并安装。  
2. 配置系统权限（麦克风、辅助功能）及快捷键。  
3. 按快捷键开始录音，结束后转录内容自动粘贴至当前窗口。  

**注意事项：**  
- 部分系统（如 Linux Wayland）需额外工具支持粘贴功能。  
- Whisper 模型在部分配置下可能崩溃，需开发者协助调试。