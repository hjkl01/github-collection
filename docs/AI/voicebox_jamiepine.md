### [voicebox](https://github.com/jamiepine/voicebox) ![GitHub Repo stars](https://img.shields.io/github/stars/jamiepine/voicebox?style=social)

Voicebox 是一个开源、可本地运行的语音合成与克隆工作室，可作为 ElevenLabs 的替代方案。它支持从短音频克隆声音、文本转语音、多语言生成、音频后期处理，并可通过时间线编辑器制作多角色语音项目。

核心功能包括：  
- **本地优先与隐私保护**：模型和语音数据保留在本机。  
- **多引擎语音克隆**：内置 5 种 TTS 引擎（Qwen3-TTS、LuxTTS、Chatterbox Multilingual、Chatterbox Turbo、TADA），可按次切换。  
- **多语言支持**：覆盖 23 种语言。  
- **情绪与拟声标签**：支持在文本中插入如 `[laugh]`、`[sigh]` 等表达标签生成更有表现力的语音。  
- **后期音效处理**：支持变调、混响、延迟、合唱/镶边、压缩、增益、高通、低通等效果，含预设与自定义预设。  
- **超长文本生成**：自动分句分块并交叉淡化拼接，最长支持 50,000 字符。  
- **版本化管理**：保留原始结果、支持效果版本、重采样 take、来源追踪与收藏。  
- **异步生成队列**：非阻塞提交、串行执行、防 GPU 争用、失败重试与崩溃恢复。  
- **语音档案管理**：支持录音/导入创建、多样本增强、导入导出、按档案设置默认效果。  
- **故事编辑器**：多轨时间线编排，适合对话、播客、叙事内容制作。  
- **录音与转写**：应用内录音、系统音频采集、Whisper 自动转写与多格式导出。  
- **模型管理与硬件支持**：可卸载模型释放显存，支持 macOS/Windows/Linux、CUDA/ROCm/DirectML/Intel Arc/CPU 与 Docker。  
- **API 优先**：提供完整 REST API，便于集成到游戏对话、播客生产、无障碍工具、语音助手和内容自动化流程中。