
---
title: librespot
---

### [librespot-org librespot](https://github.com/librespot-org/librespot)

**项目核心内容总结：**

librespot 是一个开源的 Spotify 客户端库，支持通过多种后端控制播放音乐，并作为 Spotify Connect 接收器使用，替代已弃用的官方闭源库 libspotify。仅支持 Spotify Premium 账户，不兼容免费账户功能。

**使用方法：**  
- 通过 `cargo install librespot` 安装，CLI 命令如 `librespot -n "设备名" -b 160` 可创建音频设备。  
- 构建需安装系统依赖（如 Linux 需 `libasound2-dev`），使用 `cargo build --release` 编译。  
- 支持多种音频后端（Rodio、ALSA、GStreamer 等），缓存目录需设为 `700` 权限以保障安全。

**主要特性：**  
- 提供官方库未包含的额外功能。  
- 支持多平台音频输出及自定义设备类型（如 AVR）。  
- 通过 Gitter 和 GitHub 讨论社区维护，相关项目包括 Spotifyd、raspotify 等。