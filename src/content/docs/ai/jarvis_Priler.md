
---
title: jarvis
---

### [Priler jarvis](https://github.com/Priler/jarvis)  ![GitHub Repo stars](https://img.shields.io/github/stars/Priler/jarvis?style=social)

**JARVIS 语音助手** 是一个使用神经网络技术（如语音识别、语音合成、唤醒词检测等）开发的实验性语音助手。

### 核心功能
- **完全离线运行**，不依赖云端服务；
- **开源**，代码透明；
- **不收集用户数据**，注重隐私保护；
- 支持语音转文字（STT）、文字转语音（TTS）、唤醒词检测（Wake Word）、自然语言理解（NLU）等功能；
- 当前仅支持**俄语**，未来将支持乌克兰语和英语。

### 技术栈
- 后端使用 **Rust** + **Tauri**；
- 前端使用 **Vite** + **Svelte**；
- 使用的神经网络模型包括：
  - **STT**：Vosk；
  - **TTS**：多个模型（如 Silero、Coqui、gTTS 等）目前未使用；
  - **唤醒词**：Rustpotter、Porcupine、Vosk（效率低）等；
  - **NLU**：尚未实现；
  - **聊天**：未来计划集成 ChatGPT。

### 使用方法
- 需要安装 **Rust** 和 **NodeJS**；
- 安装依赖后，使用 `cargo tauri build` 构建项目；
- 使用 `cargo tauri dev` 启动开发环境。

### 其他信息
- 旧版本是用 Python 编写的，可在 GitHub 找到；
- 使用 **CC BY-NC-SA 4.0** 协议授权。