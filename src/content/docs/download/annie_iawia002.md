
---
title: annie
---

### [iawia002 annie](https://github.com/iawia002/annie)

Lux 是一个支持多平台视频下载的命令行工具，可从包括 YouTube、优酷、TikTok、Reddit、AcFun 等 100+ 网站下载视频。主要特性包括：  
1. **跨平台支持**：覆盖主流视频网站及部分成人内容平台；  
2. **Cookie/CCODE 自定义**：通过 `-c` 参数指定 Cookie 或 `-ccode` 绕过部分网站（如优酷）的反爬限制；  
3. **开源免费**：基于 MIT 许可证，支持社区贡献代码。  

**使用方法**：  
直接通过命令行输入 `lux [URL]`，部分网站需附加 Cookie（如 `lux -c "msToken=..." URL`）。  

**注意事项**：  
- 优酷需定期更新 Cookie 或手动指定最新 CCODE；  
- 西瓜/头条视频必须携带有效 Cookie 才能下载。