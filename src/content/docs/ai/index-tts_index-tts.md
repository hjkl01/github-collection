
---
title: index-tts
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/index-tts/index-tts?style=social) ](https://github.com/index-tts/index-tts)
### [index-tts index-tts](https://github.com/index-tts/index-tts)

**项目核心内容总结：**  

1. **项目功能**  
   IndexTTS2 是一个支持情感表达和时长控制的文本到语音合成系统，可生成多语言语音，支持中文拼音控制，提供高质量、可控的语音合成能力。  

2. **使用方法**  
   - 安装依赖后，使用 uvp、vits 或 gsvits 模型进行推理。  
   - 通过参考语音、文本情感描述（如“害怕”“兴奋”）或拼音标注控制语音情感与发音。  
   - 支持调整情感强度（`emo_alpha`）、随机性（`use_random`）等参数。  

3. **主要特性**  
   - **情感与时长控制**：支持基于参考语音、文本描述或拼音的多维度情感调控。  
   - **多语言支持**：覆盖中文、英文等多种语言，兼容混合中文字符与拼音的输入。  
   - **高效推理框架**：提供快速部署与系统集成能力，适配工业级应用场景。  
   - **模型兼容性**：兼容 IndexTTS1 旧版本，支持不同模型架构（uvp、vits、gsvits）。  

4. **其他信息**  
   - 提供 HuggingFace、ModelScope 等平台的在线演示与模型下载。  
   - 依赖 NVIDIA 的 BigVGAN 等开源技术，支持社区贡献与扩展。