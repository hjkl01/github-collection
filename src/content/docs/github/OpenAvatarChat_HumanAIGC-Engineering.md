
---
title: OpenAvatarChat
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/HumanAIGC-Engineering/OpenAvatarChat?style=social) ](https://github.com/HumanAIGC-Engineering/OpenAvatarChat)
### [HumanAIGC-Engineering OpenAvatarChat](https://github.com/HumanAIGC-Engineering/OpenAvatarChat)

样的

</think>

**项目核心内容总结：**  
OpenAvatarChat 是一个集成了语音识别、语言模型、文本到语音、数字人生成等功能的开源项目，支持多模态交互。用户可以通过配置文件自定义模型参数，包括语音识别（ASR）、语言模型（LLM）、文本到语音（TTS）以及数字人生成（LiteAvatar）等模块。项目支持 Gradio 界面运行，可通过命令行指定配置文件启动服务。用户还可以通过 Docker 或脚本安装 Coturn 服务，以支持实时音视频通信。项目提供了多种模型的配置选项，并支持通过一键安装包进行快速部署。主要特性包括多模型支持、灵活配置、支持实时通信、提供一键安装包等。

---

**使用方法：**  
1. 克隆项目并安装依赖；
2. 通过配置文件设置模型路径、参数等；
3. 启动服务，可使用 Gradio 界面进行交互；
4. 可选：使用一键安装包（B站、夸克网盘等）快速部署。

**主要特性：**  
- 支持多模态交互（语音、文本、视频）；
- 提供多种模型配置（如 MiniCPM、CosyVoice、LiteAvatar 等）；
- 支持 HTTPS 通信和 Coturn 服务配置；
- 提供一键安装包，便于快速部署；
- 可通过配置文件灵活调整参数（如帧率、模型名称、语音阈值等）；
- 支持多种模型的本地或远程调用（如百炼 API、阿里云等）。