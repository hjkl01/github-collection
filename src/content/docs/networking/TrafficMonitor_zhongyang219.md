
---
title: TrafficMonitor
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/zhongyang219/TrafficMonitor?style=social) ](https://github.com/zhongyang219/TrafficMonitor)
### [zhongyang219 TrafficMonitor](https://github.com/zhongyang219/TrafficMonitor)

TrafficMonitor 是一款 Windows 平台的网速监控工具，可实时显示网络传输速率、CPU 和内存占用率，支持任务栏嵌入、皮肤更换、历史流量统计及硬件监控（温度、显卡/硬盘利用率等）。提供标准版（含全部功能，需管理员权限）和 Lite 版（无硬件监控功能，无需管理员权限）两种版本。  

**主要功能**：  
- 多网卡选择、网络详情查看  
- 任务栏窗口自定义显示内容  
- 皮肤更换与自定义（支持 XML/INI 配置及 PNG 透明背景）  
- 插件扩展（需将 DLL 放入 plugins 目录）  
- 硬件监控（依赖 LibreHardwareMonitor 库，可能增加资源占用风险）  

**使用方法**：  
启动后通过右键悬浮窗菜单切换任务栏显示，进入选项设置调整显示项、颜色、字体等。皮肤文件需存放至 `skins` 目录，插件需放至 `plugins` 目录。  

**注意事项**：  
硬件监控功能可能引发程序崩溃或系统不稳定，建议仅在必要时开启。Lite 版适合无需硬件监控的用户。