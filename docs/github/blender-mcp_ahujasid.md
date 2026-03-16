### [ahujasid blender-mcp](https://github.com/ahujasid/blender-mcp)  ![GitHub Repo stars](https://img.shields.io/github/stars/ahujasid/blender-mcp?style=social)

BlenderMCP 是通过模型上下文协议（MCP）连接 Blender 与 Claude AI 的工具，允许 AI 直接控制 Blender 进行 3D 建模与场景操作。

核心功能：
- **对象与场景控制**：创建、修改、删除 3D 物体，调整材质与颜色，获取场景详细信息。
- **交互辅助**：发送视口截图辅助 AI 理解场景，支持双向 Socket 通信。
- **代码执行**：在 Blender 中运行任意 Python 代码。
- **资源集成**：支持下载 Sketchfab 模型、Poly Haven 资产，利用 Hyper3D 和 Hunyuan3D 生成 3D 模型。
- **多环境支持**：支持本地及远程主机运行，兼容 Claude Desktop、Cursor、VS Code 等编辑器。

安装需 Blender 3.0+、Python 3.10+ 及 uv 包管理器。系统包含可关闭的匿名遥测，且因涉及代码执行存在安全风险，建议谨慎使用。