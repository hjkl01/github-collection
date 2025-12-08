
---
title: dots-hyprland
---

### [end-4 dots-hyprland](https://github.com/end-4/dots-hyprland)

该项目是 **end_4 的 Hyprland 窗口管理器配置文件**，提供以下核心功能与特性：

### **主要功能**
1. **实时预览窗口管理**：通过 "Overview" 功能展示所有打开的应用程序实时预览，支持搜索/计算/运行操作。
2. **AI 集成**：内置 Gemini API 和 Ollama 模型，支持 AI 相关功能。
3. **自动配色系统**：根据壁纸自动生成符合 Material 设计规范的美观且无障碍的配色方案。
4. **透明安装流程**：所有执行命令会在运行前显示，确保安装过程可追踪。

### **使用方法**
- **快速安装**：运行 `bash <(curl -s https://ii.clsty.link/get)`。
- **手动安装**：克隆仓库后执行 `./setup install`。
- **默认快捷键**：`Super`+`Enter` 打开终端，`Super`+`/` 查看快捷键列表。

### **技术依赖**
- **核心组件**：基于 [Hyprland](https://github.com/hyprwm/hyprland) 窗口管理器，使用 [Quickshell](https://quickshell.outfoxxed.me/) 作为小部件系统（状态栏、侧边栏等）。
- **其他依赖**：详见 [deps-info.md](https://github.com/end-4/dots-hyprland/blob/main/sdata/deps-info.md)。

### **备注**
- 明确声明不使用 Waybar，反对将其称为 "Waybar"。
- 项目提供 Discord 支持链接（https://discord.gg/GtdRBXgMwq），但建议通过 GitHub 解决问题。