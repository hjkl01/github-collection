
---
title: librespot
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/librespot-org/librespot?style=social) ](https://github.com/librespot-org/librespot)
### [librespot-org librespot](https://github.com/librespot-org/librespot)

**项目核心内容总结：**

**功能**  
librespot 是一个开源的 Spotify 客户端库，用于控制音乐播放、作为 Spotify Connect 接收器，替代已弃用的官方闭源库 libspotify，并提供额外功能（如更高音质、设备类型自定义等）。仅支持 Spotify Premium 账户，不兼容免费账户功能。

**使用方法**  
1. 通过 Cargo 安装：`cargo install librespot`。  
2. 命令行运行示例：`librespot -n "设备名" -b 320`（设置设备名和音频比特率）。  
3. 支持参数：缓存目录、音量归一化、设备类型（如 AVR）、TLS 和音频后端（如 Rodio、ALSA 等）。

**主要特性**  
- 支持多种音频后端（Rodio、ALSA、GStreamer 等）和跨平台（Linux、macOS、Windows）。  
- 提供 Spotify Connect 接收器功能，可自定义设备名称和类型。  
- 开源 MIT 许可证，支持社区维护和扩展。  
- 相关项目包括 Kodi 插件、Raspberry Pi 音乐盒、多房间音频系统等。  

**注意事项**  
- 仅限 Spotify Premium 用户使用。  
- 使用可能违反 Spotify 服务条款，需自行承担风险。