
---
title: appium
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/appium/appium?style=social) ](https://github.com/appium/appium)
### [appium appium](https://github.com/appium/appium)

Appium 是一个开源的跨平台自动化测试框架，支持原生、混合、移动网页和桌面应用的自动化测试。其核心功能包括：  
- **无需修改被测应用**，通过标准自动化 API 实现跨平台兼容；  
- **支持多种编程语言**（如 Java、Python、Ruby、C# 等）编写测试脚本；  
- **模块化设计**，通过驱动（Drivers）扩展平台支持，通过插件（Plugins）增强功能；  
- **支持并行测试**，可在单个服务器或多个进程中运行；  
- **兼容云测试平台**，如 BrowserStack、LambdaTest 等。  

**使用方法**：  
1. 通过 `npm i -g appium` 安装核心服务器；  
2. 安装对应平台的驱动（如 `appium driver install xcuitest`）；  
3. 使用 `appium server` 启动服务，通过客户端库发送 WebDriver 命令；  
4. 管理插件、驱动的安装、更新和卸载（如 `appium plugin install <name>`）。  

**主要特性**：  
- 支持 iOS、Android、macOS、Windows 等多平台；  
- 提供日志记录、赞助支持计划；  
- 采用 Apache-2.0 许可证，部分组件使用 ISC 许可证。