
---
title: manim
---

### [3b1b manim](https://github.com/3b1b/manim)  ![GitHub Repo stars](https://img.shields.io/github/stars/3b1b/manim?style=social)

**核心内容总结：**  
Manim 是一个用于创建精确数学教学动画的程序化引擎，支持通过代码生成动态演示。项目有两个版本：原始由 3Blue1Brown 作者开发的 **ManimGL**，以及社区维护的 **Manim Community**（更稳定、易用）。  

**安装方法：**  
- 通过 `pip install manimgl` 安装 ManimGL（注意包名为 `manimgl`，非 `manim`）。  
- 不同系统需额外安装 FFmpeg、LaTeX（可选）及依赖库（如 Linux 的 Pango）。  
- Windows 和 Mac 需手动配置环境并克隆仓库安装。  
- Anaconda 用户可通过创建虚拟环境安装。  

**使用方法：**  
- 运行 `manimgl example_scenes.py OpeningManimExample` 可直接测试示例动画。  
- 支持命令行参数控制输出（如 `-w` 保存文件、`-o` 自动打开结果）。  
- 可通过 `custom_config.yml` 配置输出路径、画质等参数。  

**主要特性：**  
- 支持 LaTeX 公式渲染、OpenGL 图形处理及 FFmpeg 视频导出。  
- 社区版提供更完善的文档（含中文版本）和开发支持。  
- 提供示例代码和 3Blue1Brown 视频源码参考（需注意版本兼容性）。  

**注意事项：**  
- 安装时需明确选择版本（ManimGL 或社区版），避免混淆。  
- Windows 用户需预先安装 MiKTeX 和 FFmpeg；Mac 需通过 Homebrew 安装依赖。