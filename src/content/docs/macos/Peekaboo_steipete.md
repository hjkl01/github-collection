
---
title: Peekaboo
---

### [steipete Peekaboo](https://github.com/steipete/Peekaboo)  ![GitHub Repo stars](https://img.shields.io/github/stars/steipete/Peekaboo?style=social)

**项目名称：Peekaboo（窥视）**  
**项目类型：Mac 自动化工具**  
**版本状态：3.0.0-beta4（测试版）**

---

### 一、项目功能

Peekaboo 是一个为 macOS 提供的自动化工具，具备高精度的屏幕捕捉、AI 分析和完整的 GUI 自动化能力。它支持通过自然语言进行多步骤自动化操作，并可在 CLI 和 MCP 服务器中使用。支持多屏操作，适用于开发、测试、AI 联动等场景。

---

### 二、主要特性

- **高精度屏幕捕捉**：支持窗口、菜单栏、全屏的像素级截图，可选 Retina 2x 分辨率。
- **自然语言代理**：可编写自然语言指令（如“打开备忘录并创建一个待办列表”），自动执行点击、输入、滚动等操作。
- **菜单与状态栏识别**：无需点击即可发现并操作菜单和状态栏项，返回结构化 JSON 数据。
- **多 AI 模型支持**：支持 GPT-5.1、Claude 4.x、Grok 4-fast、Gemini 2.5、本地 Ollama 模型等。
- **MCP 服务支持**：可作为 MCP 服务器运行，与 Claude Desktop、Cursor 等工具集成。
- **可配置工作流**：支持可重复的自动化脚本，具备严格的类型检查。
- **丰富的命令行工具**：包含 20+ 命令，如点击、输入、滚动、窗口管理、菜单操作、Dock 交互等。
- **权限管理**：需要 macOS 的“屏幕录制”和“辅助功能”权限。

---

### 三、安装方式

1. **Homebrew 安装（CLI + 应用）**：
   ```bash
   brew install steipete/tap/peekaboo
   ```

2. **MCP 服务（Node.js 环境）**：
   ```bash
   npx -y @steipete/peekaboo
   ```

---

### 四、使用示例

- **截图并保存**：
  ```bash
  peekaboo image --mode screen --retina --path ~/Desktop/screen.png
  ```

- **通过自然语言自动化**：
  ```bash
  peekaboo "打开备忘录并创建一个待办列表"
  ```

- **运行 MCP 服务**：
  ```bash
  npx -y @steipete/peekaboo
  ```

---

### 五、开发环境要求

- macOS 15+（Sequoia）
- Xcode 16+ / Swift 6.2
- Node.js 22+（仅用于构建脚本）

---

### 六、许可证

MIT 许可证