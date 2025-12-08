
---
title: OpenAvatarChat
---

### [HumanAIGC-Engineering OpenAvatarChat](https://github.com/HumanAIGC-Engineering/OpenAvatarChat)

**项目核心内容总结：**  
OpenAvatarChat 是一个集成语音识别（ASR）、语言模型（LLM）、文本转语音（TTS）和数字人生成的多模态交互系统，支持实时语音对话、视频生成与多模型协作。  

**主要功能与特性：**  
1. **多模型支持**：集成 MiniCPM（语言模型）、CosyVoice（TTS）、LiteAvatar（数字人）、FunASR（ASR）等模型，支持语音、文本、视频多模态交互。  
2. **灵活配置**：通过 YAML 文件配置模型路径、API 密钥、语音阈值、帧率、SSL 证书等参数，支持自定义模型替换与性能调优（如低延迟模式、GPU 使用）。  
3. **部署方式多样**：提供本地运行、Docker 部署、coturn 服务配置（支持 WebRTC 通信），并兼容社区提供的一键安装包（Windows/Linux/B站/夸克网盘）。  
4. **交互能力**：支持语音唤醒（VAD）、多轮对话、参考音频驱动音色生成（CosyVoice）、数字人实时视频生成（LiteAvatar）。  

**使用方法：**  
- 克隆项目，安装依赖，配置模型路径与 API 密钥；  
- 启动服务后通过 Gradio 界面或 WebRTC 进行交互；  
- 可选部署 Docker 容器或使用社区提供的一键包快速部署。  

**关键配置参数**：日志级别、服务地址/端口、SSL 证书路径、模型选择（如 MiniCPM-o-2_6）、语音识别阈值、数字人帧率（LiteAvatar）等。