
---
title: go-ios
---

### [danielpaulus go-ios](https://github.com/danielpaulus/go-ios)  ![GitHub Repo stars](https://img.shields.io/github/stars/danielpaulus/go-ios?style=social)

go-ios 是一款基于 Go 语言的跨平台开源工具，可在 Linux、Windows 和 macOS 上自动化管理 iOS 设备，旨在提供稳定且生产就绪的解决方案。

主要功能包括：
- **应用管理**：支持 IPA 或应用包安装、应用启动/停止、运行 XCTests 和 WebdriverAgent。
- **设备控制**：实现免提配对、开发者镜像自动下载与挂载、设备状态配置（网络模拟、热状态）、系统重启与擦除。
- **调试与维护**：提供调试代理、日志获取（syslog/crash）、文件同步、截图及网络抓包。
- **信息查询**：获取设备详情、电池、磁盘空间、锁屏数据及系统状态。
- **高级特性**：支持 iOS 17+ 隧道连接、辅助功能控制、位置模拟、监管设备配置及 HTTP 代理设置。

项目所有命令默认输出 JSON 格式，支持模块集成，便于与其他编程环境对接。