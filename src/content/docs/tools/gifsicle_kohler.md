
---
title: gifsicle
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/kohler/gifsicle?style=social) ](https://github.com/kohler/gifsicle)
### [kohler gifsicle](https://github.com/kohler/gifsicle)

**项目核心内容总结：**  
Gifsicle 是一个用于处理 GIF 图像的工具，支持合并/拆分 GIF 动画、调整帧属性（如延迟、透明度、颜色映射）、优化动画体积、添加注释等功能。配套工具 gifview 可显示 GIF 动画，gifdiff 可比对 GIF 视觉差异。  

**使用方法：**  
- **UNIX 系统**：通过 `./configure` 和 `make` 编译安装，支持禁用 gifview/gifdiff。  
- **Windows 系统**：使用 Visual C 或 Borland C++ 通过 `nmake` 编译（需修改对应 Makefile）。  

**主要特性：**  
- 支持动画帧操作、优化压缩、颜色调整等；  
- 跨平台（UNIX/Windows）；  
- 提供命令行工具及配套程序（gifview/gifdiff）；  
- 开源，遵循 GNU GPL v2 许可证。