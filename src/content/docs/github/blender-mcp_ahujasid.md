
---
title: blender-mcp
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/ahujasid/blender-mcp?style=social) ](https://github.com/ahujasid/blender-mcp)
### [ahujasid blender-mcp](https://github.com/ahujasid/blender-mcp)

**项目功能**  
BlenderMCP 通过 Model Context Protocol（MCP）将 Blender 与 Claude AI 连接，实现 Claude 对 Blender 的交互控制，支持提示辅助的 3D 建模、场景创建与操作，包括对象创建/修改、材质控制、场景信息获取及 Python 代码执行。

**使用方法**  
1. **安装依赖**：需 Blender 3.0+、Python 3.10+ 及 uv 包管理器（Mac/Windows 安装方式不同）。  
2. **配置环境变量**：设置 `BLENDER_HOST` 和 `BLENDER_PORT`（默认 localhost:9876）。  
3. **安装 Blender 插件**：下载 `addon.py` 并在 Blender 中启用。  
4. **集成到 Claude/Cursor**：修改 Claude 的 `claude_desktop_config.json` 或 Cursor 的 MCP 配置，添加 `uvx blender-mcp` 命令启动服务器。  

**主要特性**  
- 双向通信：通过 socket 实现 Claude 与 Blender 的实时交互。  
- 对象与材质控制：支持创建、修改对象及材质。  
- 场景分析：获取当前 Blender 场景的详细信息。  
- 代码执行：可运行任意 Python 代码操作 Blender。  
- 资源支持：集成 Poly Haven 资产、Hyper3D Rodin 模型生成及 Sketchfab 模型下载。  

**注意事项**  
- 避免同时在 Claude 和 Cursor 中运行 MCP 服务器。  
- 执行代码工具可能带来风险，需谨慎使用。  
- 复杂操作建议拆分为小步骤执行。