
---
title: ebook2audiobook
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/DrewThomasson/ebook2audiobook?style=social) ](https://github.com/DrewThomasson/ebook2audiobook)
### [DrewThomasson ebook2audiobook](https://github.com/DrewThomasson/ebook2audiobook)

**项目核心内容总结：**  
ebook2audiobook 是一个将电子书转换为有声书的工具，支持多种格式（如 EPUB、MOBI、PDF 等）和输出格式（如 M4B、MP3、WAV 等）。主要功能包括：  
1. **多格式支持**：自动识别电子书章节，支持 20+ 种电子书格式，推荐使用 EPUB/MOBI 以获得最佳章节分割效果。  
2. **语音合成**：基于 XTTSv2 等模型实现文本转语音，支持自定义微调模型和语音参考音频。  
3. **GPU 加速**：通过 Docker 容器支持 GPU 加速，显著提升转换速度。  
4. **灵活部署**：提供本地脚本运行、Docker 部署（含无头模式）及 Compose 配置选项，支持自定义参数（如输出格式、GPU 配置）。  
5. **便捷操作**：支持通过 Web 界面上传电子书并转换，或使用命令行参数实现无头模式批量处理。  

**使用方法**：  
- **本地运行**：克隆仓库后执行脚本，通过 `--help` 查看参数。  
- **Docker 部署**：修改 `docker-compose.yml` 配置后启动容器，支持 GPU 启用/禁用、镜像版本控制等。  
- **特殊功能**：添加 `###` 或 `[pause]` 可插入静音间隔，支持自定义配置文件调整参数。  

**主要特性**：  
- 支持多语言、多模型（如 XTTSv2、Coqui TTS）及自定义微调模型。  
- 提供 Docker 镜像和 Compose 模板，便于部署和扩展。  
- 可通过 Web 界面交互操作，或直接使用命令行实现自动化处理。