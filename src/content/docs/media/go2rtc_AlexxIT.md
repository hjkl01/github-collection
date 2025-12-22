
---
title: go2rtc
---

### [AlexxIT go2rtc](https://github.com/AlexxIT/go2rtc)  ![GitHub Repo stars](https://img.shields.io/github/stars/AlexxIT/go2rtc?style=social)

**项目核心内容总结：**

**功能**  
go2rtc 是一个支持多协议（RTSP、FFmpeg 等）的流媒体处理工具，主要用于音视频流的接收、转码、多源编解码协商及分发。支持与 Home Assistant、Frigate 等系统集成，适用于安防监控、智能家庭等场景。

**主要特性**  
1. **多源编解码协商**：自动匹配不同设备（如摄像头、FFmpeg）与播放端（如浏览器）的音视频编码格式，实现跨设备兼容。  
2. **音频转码**：支持将低质量 PCM/PCMU/PCMA 音频转为 OPUS/AAC，提升播放兼容性；RTSP 流中 FLAC 编码需通过 FFmpeg 转码为 AAC。  
3. **低延迟播放**：提供 FFplay/VLC 等工具的低延迟播放参数配置。  
4. **硬件加速**：支持通过 FFmpeg 调用 GPU 等硬件加速编解码。  
5. **跨平台支持**：可在 Alpine Linux、Arch、Synology 等系统部署。  

**使用方法**  
1. 通过 YAML 配置文件定义流源（如 RTSP、FFmpeg 转码链），并设置编解码参数。  
2. 集成至 Home Assistant、Frigate 等系统，实现监控画面展示、录像存储等功能。  
3. 使用 FFplay 或 VLC 播放流媒体，调整缓存参数降低延迟。  

**适用场景**  
- 安防摄像头流媒体接入与优化（如 Dahua、Eufy 等设备）。  
- 多设备音视频格式兼容性处理（如浏览器播放 RTSP 流）。  
- 智能家居系统（Home Assistant）与 AI 视频分析（Frigate）的联动。