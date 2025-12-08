
---
title: buzz
---

### [chidiwilliams buzz](https://github.com/chidiwilliams/buzz)

**项目核心内容总结：**

**功能**  
Buzz 是一款支持离线音频转录与翻译的工具，基于 OpenAI 的 Whisper 技术，可在个人电脑上运行。Mac 版本提供原生界面、音频播放、拖拽导入、字幕编辑、搜索等功能。

**使用方法**  
1. **macOS/Windows/Linux**：通过 SourceForge 下载安装包（Windows 需手动运行安装程序）。  
2. **Linux**：支持 Flatpak 或 Snap 安装（需提前安装依赖库）。  
3. **PyPI**：通过 `pip install buzz-captions` 安装，需先安装 ffmpeg；若需 GPU 加速，需额外安装 CUDA 相关库。  
4. **开发版**：通过官方文档获取最新版本。  

**主要特性**  
- 离线处理音频，无需网络连接；  
- 支持多平台（Mac、Windows、Linux）；  
- 提供 App Store 的 Mac 专用版本（含优化功能）；  
- 支持 GPU 加速（PyPI 版需配置 CUDA）。