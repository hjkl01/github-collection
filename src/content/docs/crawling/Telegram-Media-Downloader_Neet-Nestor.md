
---
title: Telegram-Media-Downloader
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/Neet-Nestor/Telegram-Media-Downloader?style=social) ](https://github.com/Neet-Nestor/Telegram-Media-Downloader)
### [Neet-Nestor Telegram-Media-Downloader](https://github.com/Neet-Nestor/Telegram-Media-Downloader)

**项目核心内容总结：**  
Telegram Media Downloader 是一个用户脚本，用于解锁 Telegram 网页版（Webapp）中被限制下载的媒体内容（图片、GIF、音频、视频），支持从频道、聊天和故事中下载文件。  

**主要功能：**  
1. **突破下载限制**：在 Telegram Webapp 的频道或聊天中，即使官方禁用下载功能，也可通过该脚本恢复下载按钮。  
2. **支持多版本 Webapp**：兼容 Telegram 的两个网页版（https://webk.telegram.org 和 https://webz.telegram.org），其中音频消息下载等特性仅在 /k/ 版本可用。  
3. **视频进度条**：下载视频时显示右下角进度条，图片和音频无进度条。  

**使用方法：**  
1. 安装用户脚本管理器（如 Tampermonkey 或 Violentmonkey）。  
2. 通过 Greasy Fork 安装脚本（链接：https://greasyfork.org/scripts/446342-telegram-media-downloader），或手动导入 `src/tel_download.js`。  
3. 仅在 Telegram Webapp 使用，受限内容可通过脚本添加的下载按钮获取。  

**注意事项：**  
- 部分功能依赖 Webapp 版本，建议优先使用 /k/ 版本。  
- 官方已开放下载的场景无需脚本。