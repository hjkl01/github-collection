### [ntdevlabs tiny11builder](https://github.com/ntdevlabs/tiny11builder)  ![GitHub Repo stars](https://img.shields.io/github/stars/ntdevlabs/tiny11builder?style=social)

tiny11builder 是一个基于 PowerShell 的开源脚本工具，用于自动化构建精简版 Windows 11 镜像。其核心功能总结如下：

1. **广泛兼容性**：支持任意 Windows 11 发布版本、语言及架构（如 x64/arm64）。
2. **双版本构建模式**：
   - **常规版 (tiny11maker.ps1)**：移除大量预装应用（如 Edge、OneDrive、Xbox 等）但保留系统服务性，支持后期添加语言、更新和功能，适合日常使用。
   - **核心版 (tiny11coremaker.ps1)**：更激进地移除系统组件（包括 WinSxS 组件库、Windows Defender、Windows Update 等），生成的镜像体积更小但不可维护（无法添加更新或功能），专为快速测试或开发环境设计。
3. **优化与自动化**：利用 DISM 恢复压缩技术减小最终 ISO 体积，集成无人值守应答文件以自动跳过微软账户登录，无需依赖外部工具即可完成制作。