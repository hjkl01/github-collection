
---
title: fyne
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/fyne-io/fyne?style=social) ](https://github.com/fyne-io/fyne)
### [fyne-io fyne](https://github.com/fyne-io/fyne)

**核心内容总结：**  
Fyne 是一个用 Go 语言编写的跨平台 UI 工具包，支持桌面和移动设备应用开发。用户可通过单个代码库实现多平台应用构建，提供丰富的组件和示例。  

**使用方法：**  
1. 安装 Go 1.17 或更高版本及 C 编译器。  
2. 使用 `go get fyne.io/fyne/v2@latest` 安装核心库。  
3. 运行示例代码（如 `go run main.go`）快速启动应用。  
4. 使用 `fyne_demo` 查看组件示例。  
5. 通过 `fyne package` 打包移动应用，使用 `fyne install` 安装到设备。  

**主要特性：**  
- 跨平台支持（桌面、移动设备）。  
- 提供移动设备模拟模式。  
- 支持应用打包、签名及发布到应用商店。  
- 包含额外工具（如 `fyne_settings`）优化开发体验。  
- Linux/BSD 用户可安装 FyneDesk 作为桌面环境。  

**注意事项：**  
首次编译可能耗时较长（如 Windows 平台需 10 分钟），后续构建速度较快。