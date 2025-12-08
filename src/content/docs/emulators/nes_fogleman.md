
---
title: nes
---

### [fogleman nes](https://github.com/fogleman/nes)

**核心内容总结：**  
该项目是一个用Go语言编写的NES（任天堂娱乐系统）模拟器，支持运行NES游戏ROM文件。  

**功能与特性：**  
1. **模拟器功能**：支持多种NES游戏ROM格式（如NROM、MMC1、MMC3等），覆盖约85%的NES游戏。  
2. **图形与音频**：基于OpenGL（依赖`go-gl`库）渲染画面，使用PortAudio库处理音频。  
3. **用户交互**：支持键盘和手柄控制，键盘映射包括方向键、Enter（开始）、Shift（选择）、Z/X（AB按钮）等。  

**使用方法：**  
- 安装依赖：需先安装系统级的PortAudio库（如Ubuntu用`apt-get install portaudio19-dev`，Mac用`brew install portaudio`）。  
- 安装模拟器：通过`go get github.com/fogleman/nes`自动下载依赖并编译。  
- 运行方式：  
  - 不指定参数时，在当前目录搜索ROM文件。  
  - 指定目录时，在目录中搜索ROM文件。  
  - 指定单个ROM文件时直接运行该游戏。  
  - 菜单界面会通过ROM文件的MD5哈希值从在线数据库下载缩略图。  

**已知问题：**  
- PPU（画面处理单元）时序存在轻微误差，但多数游戏可正常运行。  
- APU（音频处理单元）模拟尚未完全精确。  

**依赖项：**  
- Go语言环境。  
- 系统级PortAudio库。  
- Go库：`go-gl/gl`、`go-gl/glfw`、`portaudio`。