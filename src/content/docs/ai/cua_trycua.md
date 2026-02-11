
---
title: cua
---

### [trycua cua](https://github.com/trycua/cua)  ![GitHub Repo stars](https://img.shields.io/github/stars/trycua/cua?style=social)

**项目名称**：Cua

**核心内容总结**：

Cua 是一个用于构建、测试和部署**能够使用计算机的智能代理（Agent）**的平台。它提供了一系列工具和 SDK，帮助开发者实现**图形界面自动化、代码执行、虚拟化管理**等功能，并支持多种主流 AI 模型和开发环境。

---

### **主要功能与组件**：

1. **cuabot**  
   - 多代理计算机使用沙箱 CLI 工具。
   - 支持在隔离环境中运行任何 AI 代理（如 Claude Code、OpenClaw）或 GUI 流程（如浏览器操作、截图、点击等）。
   - 提供 H.265 视频流、共享剪贴板和音频功能，窗口显示在本地桌面。

2. **Cua SDK**  
   - 提供构建计算机使用代理的框架。
   - 支持图像识别、鼠标点击、键盘输入、代码执行等操作。
   - 示例：使用 Python SDK 控制虚拟环境完成任务。

3. **Cua-Bench**  
   - 用于评估计算机使用代理的基准测试平台。
   - 支持多种测试环境（如 OSWorld、ScreenSpot）和自定义任务。
   - 支持轨迹导出用于训练模型。

4. **Lume**  
   - macOS/Linux 虚拟化工具，基于 Apple 的 Virtualization.Framework。
   - 支持在 Apple Silicon 上高性能运行虚拟机。
   - 提供 Docker 兼容接口（Lumier）。

---

### **使用方法简要**：

- 安装并启动 cuabot：
  ```bash
  npx cuabot
  ```

- 运行代理或 GUI 操作：
  ```bash
  cuabot claude
  cuabot chromium
  cuabot --screenshot
  ```

- 使用 Python SDK：
  ```python
  from computer import Computer
  from agent import ComputerAgent
  agent = ComputerAgent(model="anthropic/claude-sonnet-4-5-20250929", computer=computer)
  ```

- 使用 Cua-Bench 运行测试：
  ```bash
  cb run dataset datasets/cua-bench-basic --agent cua-agent
  ```

- 使用 Lume 启动 macOS 虚拟机：
  ```bash
  lume run macos-sequoia-vanilla:latest
  ```

---

### **主要特性**：

- 支持多种 AI 模型和代理框架；
- 提供图形界面自动化与代码执行环境；
- 沙箱隔离，保障系统安全；
- 跨平台支持（Linux/macOS）；
- 提供基准测试与训练数据导出；
- 支持 Apple Silicon 高性能虚拟化；
- 社区活跃，提供文档、博客和 Discord 支持。