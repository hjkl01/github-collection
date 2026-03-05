
---
title: vhs
---

### [charmbracelet vhs](https://github.com/charmbracelet/vhs)  ![GitHub Repo stars](https://img.shields.io/github/stars/charmbracelet/vhs?style=social)

VHS 是一个将终端动画录制编写为代码的工具，主要用于 CLI 工具的演示和集成测试。它通过 `.tape` 脚本文件定义虚拟终端的操作指令（如键入命令、按键、等待等），支持自定义字体、主题、窗口尺寸及动画参数。VHS 可生成 GIF、MP4、WebM 等多种格式的动画输出，同时具备录制现有终端操作、发布在线 GIF、SSH 远程服务及 CI/CD 集成（生成金色文件）的功能，运行需依赖 `ttyd` 和 `ffmpeg`。