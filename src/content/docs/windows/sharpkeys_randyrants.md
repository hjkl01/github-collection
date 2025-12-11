
---
title: sharpkeys
---

### [randyrants sharpkeys](https://github.com/randyrants/sharpkeys)

**项目核心内容总结：**  

**功能**  
SharpKeys 是一个用于 Windows 键盘按键映射的工具，通过修改注册表实现按键重映射（如将 Caps Lock 映射为 Shift 键）。支持单键映射、多键互换（如交换 Win 键与 Ctrl 键），但不支持组合键（如 Ctrl+C 映射为其他键）或鼠标操作。  

**使用方法**  
1. 安装：通过 GitHub 发布页、Microsoft Store、winget 或 scoop 安装。  
2. 启动程序，添加或编辑按键映射。  
3. 点击“写入注册表”，重启系统使设置生效。  

**主要特性**  
- 支持 Windows 2000 至 Windows 11。  
- 提供“Type Key”功能自动识别大部分按键，但 Alt 键需手动选择。  
- 不支持 Fn 键、鼠标按键、三字节扫描码（如部分硬件专用键）。  
- 提供常见键盘布局的预设配置（如 Colemak、Surface 键盘）。  

**注意事项**  
- 误操作可能导致无法登录（如禁用 Delete 键），需通过安全模式或命令行删除注册表项 `Scancode Map` 恢复。  
- 部分硬件键（如 Logitech 音量键、Office 键）无法映射，需使用其他工具（如 PowerToys）。  
- 不支持跨用户映射，修改影响全机。