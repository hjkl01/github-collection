
---
title: MoneyPrinterTurbo
---

### [harry0703 MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)

**项目核心内容总结：**

**功能**  
MoneyPrinterTurbo 是一个基于大语言模型（LLM）的视频自动生成工具，支持文本生成、语音合成、字幕生成、背景音乐匹配等功能，可一键生成带配音和字幕的视频。

**使用方法**  
1. **部署方式**  
   - Docker：通过 `docker-compose up` 一键启动服务。  
   - 手动部署：创建虚拟环境，安装依赖（如 ImageMagick、FFmpeg），配置 `config.toml` 文件后运行 `webui.bat` 或 `webui.sh` 启动 Web 界面，或通过 `main.py` 启动 API 服务。  

2. **配置**  
   - 修改 `config.toml` 设置 LLM 提供商（如 Azure、Whisper）、Pexels API 密钥、语音路径、字幕生成方式（Edge 或 Whisper）等。  

**主要特性**  
- **多语音支持**：集成 Azure、本地等多种语音合成方案，支持 9 种 Azure 声音（需 API Key）。  
- **字幕生成**：提供 Edge（快速但质量不稳定）和 Whisper（高质量但需下载 3GB 模型）两种模式。  
- **资源管理**：内置背景音乐（`resource/songs`）和字幕字体（`resource/fonts`），支持自定义替换。  
- **API 接口**：提供 RESTful API（`http://localhost:8080`）供外部调用。  
- **跨平台兼容**：支持 Windows、macOS、Linux 系统，Docker 部署简化环境配置。  

**适用场景**  
适用于需要批量生成带配音、字幕的宣传视频、教学视频等内容的用户，支持通过 Web 界面或 API 调用实现自动化生产。