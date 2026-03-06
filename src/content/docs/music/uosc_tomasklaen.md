
---
title: uosc
---

### [tomasklaen uosc](https://github.com/tomasklaen/uosc)  ![GitHub Repo stars](https://img.shields.io/github/stars/tomasklaen/uosc?style=social)

uosc 是一款面向 MPV 播放器的高功能极简主义近距离感知 UI 界面。

核心功能：
1. 智能 UI：界面元素根据鼠标距离显示或隐藏，时间线可用时自动最小化，支持章节可视化。
2. 媒体控制：提供字幕（含在线下载与加载）、音轨、视频轨道选择及流媒体质量切换。
3. 交互增强：所有菜单支持即时搜索，鼠标滚轮可控制进度、音量、速度，集成 thumbfast 提供高性能缩略图。
4. 导航管理：支持播放列表、目录导航、文件打开及剪贴板操作。

配置与扩展：
1. 自定义菜单：通过 MPV 的 input.conf 文件注释即可构建支持嵌套的上下文菜单。
2. 命令系统：提供丰富的绑定命令（如 UI 闪显、进度切换），方便自定义快捷键。
3. 脚本 API：开放接口供第三方脚本集成或使用其渲染能力。
4. 跨平台支持：内置 Go 二进制工具处理复杂任务（如字幕搜索、剪贴板），无需额外运行时依赖。

需 MPV 0.33 及以上版本。