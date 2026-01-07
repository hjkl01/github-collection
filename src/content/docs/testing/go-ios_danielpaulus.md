
---
title: go-ios
---

### [danielpaulus go-ios](https://github.com/danielpaulus/go-ios)  ![GitHub Repo stars](https://img.shields.io/github/stars/danielpaulus/go-ios?style=social)

**项目核心内容总结：**

**项目功能：**  
go-ios 是一个跨平台命令行工具，支持与 iOS 设备进行深度交互，功能包括设备管理（重启、配对、截图）、自动化测试（运行 XCTest/XCUITest、WebDriverAgent）、系统设置（定位模拟、语言切换、时间格式调整）、网络分析（抓包、隧道建立）等。

**使用方法：**  
通过命令行输入 `ios [命令]` 调用功能，例如：  
- `ios list` 查看连接设备列表  
- `ios reboot` 重启设备  
- `ios runtest --bundle-id=com.example.app` 运行指定应用的测试  
- `ios setlocation --lat=40.73 --lon=-73.93` 设置设备虚拟位置  

**主要特性：**  
1. **自动化测试支持**：集成 XCTest/XCUITest、WebDriverAgent，支持参数化测试、日志输出。  
2. **设备管理能力**：支持设备配对、证书生成、系统重启、截图及实时视频流。  
3. **网络工具**：提供网络抓包（pcap）、隧道建立（tunnel）、RSD 服务端口查询。  
4. **系统模拟**：可模拟位置（GPS/GPX）、语言、时间格式、系统内存限制等。  
5. **跨平台兼容**：支持 macOS、Linux 等系统，部分功能需管理员权限（如隧道建立）。