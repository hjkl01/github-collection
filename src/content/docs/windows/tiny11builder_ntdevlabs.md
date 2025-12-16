
---
title: tiny11builder
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/ntdevlabs/tiny11builder?style=social) ](https://github.com/ntdevlabs/tiny11builder)
### [ntdevlabs tiny11builder](https://github.com/ntdevlabs/tiny11builder)

**核心内容总结：**  
tiny11builder 是一个使用 PowerShell 的开源脚本工具，用于自动化构建精简版 Windows 11 镜像。  

**功能：**  
- 提供两种脚本：  
  - **tiny11maker.ps1**：移除预装应用（如 Edge、OneDrive、邮件、地图等），保留系统可维护性（支持后续添加语言、更新或功能）。  
  - **tiny11coremaker.ps1**：进一步移除系统组件（如 WinSxS、Windows Defender、Windows Update 等），生成更小镜像，但无法后续扩展。  
- 使用 DISM 的恢复压缩技术减少 ISO 体积，仅依赖 Windows ADK 的 oscdimg.exe 生成启动 ISO。  
- 内置无人应答文件，跳过 Microsoft 账户登录并启用压缩安装。  

**使用方法：**  
1. 下载 Windows 11 ISO 并挂载。  
2. 以管理员身份运行 PowerShell 5.1，设置执行策略为 `Bypass`。  
3. 执行脚本，指定 ISO 挂载盘符和临时存储盘符。  
4. 选择镜像版本（SKU），脚本会自动生成 `tiny11.iso`。  

**主要特性：**  
- 支持任意 Windows 11 版本、语言和架构。  
- 移除冗余应用（如 Clipchamp、Xbox、Solitaire 等）。  
- 核心脚本移除 WinSxS 和系统更新功能，适合开发测试。  
- 可选启用 .NET 3.5 支持。  

**注意事项：**  
- Edge 和 OneDrive 有残留文件，需手动清理。  
- arm64 版本可能因缺少 OneDriveSetup.exe 导致脚本报错。  
- Outlook、Dev Home 等应用可能重新出现。