
---
title: pyautogui
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/asweigart/pyautogui?style=social) ](https://github.com/asweigart/pyautogui)
### [asweigart pyautogui](https://github.com/asweigart/pyautogui)

**PyAutoGUI核心内容总结：**  
PyAutoGUI是一个跨平台的Python模块，用于自动化控制鼠标和键盘操作，支持Windows、macOS和Linux系统。主要功能包括：  
1. **鼠标键盘控制**：移动鼠标、点击、输入文字、模拟按键及组合键（如Ctrl+C）。  
2. **消息框交互**：提供警报框、确认框、输入框和密码输入框功能。  
3. **截图与图像定位**：通过Pillow库截图，并可定位屏幕中的图像位置后自动点击。  

**使用方法**：  
- 安装：`pip install pyautogui`。  
- 示例代码：如`pyautogui.moveTo(100, 150)`移动鼠标，`pyautogui.write('Hello')`输入文字。  

**主要特性**：  
- 跨平台兼容，支持多操作系统。  
- 自动处理图像定位与坐标计算（如`locateCenterOnScreen`）。  
- 依赖库按系统自动适配（如macOS需`pyobjc`，Linux需`python3-xlib`）。  

**依赖要求**：  
- Windows无额外依赖。  
- macOS需安装`pyobjc-core`和`pyobjc`。  
- Linux需`python3-xlib`及Pillow相关库。