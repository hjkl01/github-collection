
---
title: Fabric
---

### [danielmiessler Fabric](https://github.com/danielmiessler/Fabric)

**Fabric 项目核心内容总结：**

Fabric 是一个用于与 AI 模型交互的工具，支持多种功能和特性：

1. **核心功能**  
   - 提供预设的提示模板（Patterns），用户可直接使用这些模板进行文本分析、代码生成等任务。  
   - 支持自定义模式（Custom Patterns），用户可创建专属提示模板，且自定义内容不会被项目更新覆盖。  
   - 集成多种提示策略（如“Chain of Thought”），提升 AI 模型的推理和生成效果。

2. **使用方法**  
   - 通过命令行调用，如 `fabric --pattern <模板名>` 使用预设模板，`fabric --setup` 初始化配置。  
   - 支持将剪贴板内容通过 `pbpaste` 等工具输入到 Fabric 中处理。  
   - 提供 Web 界面作为图形化操作替代方案。

3. **主要特性**  
   - **模块化设计**：预设模板与自定义模式分离，确保用户内容独立。  
   - **辅助工具**：集成 `to_pdf`（LaTeX 转 PDF）、`code_helper`（代码分析）等实用工具。  
   - **策略扩展**：支持多种提示策略，增强模型表现。  
   - **跨平台支持**：兼容 Windows、Linux、macOS，提供 PowerShell 和 Linux 命令行适配方案。

4. **安装与配置**  
   - 使用 Go 安装 Fabric 及其辅助工具（如 `go install github.com/danielmiessler/fabric/cmd/to_pdf@latest`）。  
   - 初始化时可设置自定义模式目录，确保用户内容安全。

5. **社区与贡献**  
   - 由 Daniel Miessler 创建，多位开发者（如 Jonathan Dunn、Andre Guerra）参与贡献。  
   - 提供 GitHub 贡献者列表及 Web 界面安装说明。