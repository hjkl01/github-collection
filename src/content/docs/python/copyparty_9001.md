
---
title: copyparty
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/9001/copyparty?style=social) ](https://github.com/9001/copyparty)
### [9001 copyparty](https://github.com/9001/copyparty)

**项目核心内容总结**  
copyparty 是一个跨平台文件共享工具，支持通过 HTTP 进行文件传输、媒体信息提取、音频转码及缩略图生成。主要功能包括：  
1. **多平台支持**：可在 Windows（需 Python 或独立 EXE）、Android（Termux）、iOS（a-Shell）等系统运行。  
2. **使用方法**：  
   - Windows：通过 Python 脚本（推荐）或独立 EXE（存在安全风险）运行；  
   - Android：安装 Termux 并执行脚本；  
   - iOS：使用 a-Shell 安装并配置。  
3. **特性**：  
   - 支持生成二维码（用于访问外部 IP）；  
   - 提供多种缩略图生成方式（FFmpeg、VIPS）；  
   - 包含不同版本（sfx、exe、pyz）以适应不同需求；  
   - 可通过 `/?stack` 查看线程堆栈以排查冻结问题。  

**注意事项**  
- 独立 EXE 版本（如 copyparty32.exe）因使用旧版 Python，存在安全风险，不建议用于联网环境；  
- 推荐使用 sfx 版本（依赖系统 Python），可获得更好性能与安全性；  
- 报告问题需通过 GitHub、GitLab 或 Codeberg 提交，附带日志及上下文信息。