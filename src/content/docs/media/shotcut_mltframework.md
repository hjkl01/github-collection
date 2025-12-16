
---
title: shotcut
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/mltframework/shotcut?style=social) ](https://github.com/mltframework/shotcut)
### [mltframework shotcut](https://github.com/mltframework/shotcut)

**项目功能**  
Shotcut 是一款免费、开源、跨平台的视频编辑软件，依赖 MLT、Qt6、FFmpeg 等多媒体框架和库，支持视频剪辑、音频播放等功能。

**使用方法**  
1. **安装**：可直接从官网下载预编译的二进制文件。  
2. **开发构建**：  
   - 通过 Qt Creator 快速构建测试开发版。  
   - 命令行构建需先配置依赖库路径，执行 `cmake` 配置、`cmake --build .` 编译、`cmake --install .` 安装（否则可能因找不到 QML 文件导致运行失败）。

**主要特性**  
- 依赖核心库：MLT、Qt6（最低 6.4）、FFTW、FFmpeg、frei0r、SDL 等。  
- 支持多平台（Linux、macOS、Windows）。  
- 提供功能列表和开发路线图（官网链接）。  

**其他信息**  
- **许可证**：GPLv3。  
- **翻译**：通过 Transifex 平台贡献多语言版本。  
- **构建警告**：源码构建仅建议开发者或测试者操作。