
---
title: xiaomusic
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/hanxi/xiaomusic?style=social) ](https://github.com/hanxi/xiaomusic)
### [hanxi xiaomusic](https://github.com/hanxi/xiaomusic)

**项目核心内容总结：**

1. **功能**  
   xiaomusic 是一个通过语音指令控制小米音箱播放本地和网络音乐的工具，支持多种音频格式（如 MP3、FLAC、WAV 等），并提供网络歌单、音乐转换、自定义指令等功能。

2. **使用方法**  
   - 通过 Docker 或 Docker Compose 部署服务。  
   - 配置本地音乐目录和网络歌单（支持 JSON 或 M3U 文件）。  
   - 通过 Web 界面或配置文件调整参数（如密码、主题、兼容模式等）。  
   - 语音指令控制音箱播放（如“播放歌单名称”或“转换为 MP3”）。

3. **主要特性**  
   - **兼容性**：支持主流小米音箱型号（如 L16A、LX06 等），部分型号需开启兼容模式。  
   - **格式支持**：本地音乐支持 MP3、FLAC 等格式，自动转换为 MP3 以适配不兼容设备。  
   - **网络歌单**：可通过 JSON 文件或链接添加网络电台和歌曲，附带 M3U 转换工具。  
   - **自定义指令**：用户可定义语音指令（如“播放本地音乐”）。  
   - **多主题支持**：提供多种 UI 主题（如 Tailwind、SoundScape 等）。  
   - **安全设置**：支持密码登录，防止公网环境下账号泄露。

4. **注意事项**  
   - 部分音箱（如 L05B、L16A）不支持 FLAC 格式，需开启“转换为 MP3”选项。  
   - 避免在公网环境下使用未加密的访问方式，防止小米账号泄露。  
   - 不建议绑定小米账号的摄像头设备，以防隐私风险。  
   - 项目为开源工具（MIT 许可），仅供学习研究，不承担使用风险。