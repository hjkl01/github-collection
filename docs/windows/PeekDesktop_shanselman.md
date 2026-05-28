### [PeekDesktop](https://github.com/shanselman/PeekDesktop) ![GitHub Repo stars](https://img.shields.io/github/stars/shanselman/PeekDesktop?style=social)

PeekDesktop 是一个面向 Windows 10/11 的轻量工具，复刻了 macOS Sonoma“点击桌面壁纸显示桌面”的体验：点击空白桌面或空白任务栏区域即可隐藏窗口并显示桌面，再点击应用、任务栏或壁纸可一键恢复所有窗口到原位置（含最大化状态）。  
项目支持避免误触（点击/拖动桌面图标不会触发）、可选双击触发、游戏/全屏自动暂停、任务栏触发开关、开机自启、托盘菜单控制、自动检查与就地自动更新。  

其默认模式使用 Explorer 原生“显示桌面”，并提供实验性 Fly Away 动画模式。  
技术上基于 Win32 API（如全局鼠标钩子、命中测试、窗口枚举与恢复、前台窗口事件监听等）实现，无需管理员权限，空闲内存占用低（<5MB），并提供 x64/ARM64 自包含单文件发布（Native AOT）。