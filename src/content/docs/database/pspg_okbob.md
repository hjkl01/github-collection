
---
title: pspg
---

### [okbob pspg](https://github.com/okbob/pspg)

**项目核心内容总结：**  

**功能**  
pspg 是一个用于 PostgreSQL 的命令行客户端工具，支持 Unicode 编码、多语言字符显示及丰富的表格格式（如圆角、粗边框等），可处理大文本数据，支持鼠标操作，并兼容多种终端环境（如 KDE konsole、WSL2 等）。  

**使用方法**  
- 安装方式：支持通过 Homebrew（Linux/Mac）、Debian/Ubuntu、Fedora、Alpine Linux、Arch Linux、FreeBSD、OpenBSD 等系统的包管理器安装，或从源码编译。  
- 配置：通过设置 `PSQL_PAGER` 环境变量（如 `pspg -b -X`）或命令行参数（如 `--csv`）调整输出格式。  
- 使用场景：连接 PostgreSQL 数据库，执行查询并以表格、CSV 等格式显示结果。  

**主要特性**  
1. **多终端兼容**：支持 true color 主题、鼠标操作（需终端支持），并适配不同操作系统（包括 Windows 通过 WSL2）。  
2. **显示优化**：提供多种表格模式（如 `rounded`、`heavy`），支持隐藏列、调整列宽、循环遍历列等。  
3. **扩展性**：支持通过 `st_menu` 库实现 CUA 菜单栏，便于用户交互操作。  
4. **跨平台安装**：提供多种系统的安装方式，包括源码编译（需依赖 `ncursesw` 库）及包管理器安装。  

**注意事项**  
- 安装时需确保系统已安装 `ncursesw` 开发库，部分系统需手动设置环境变量（如 `TERM=xterm-direct` 适配 true color）。  
- Windows 平台建议通过 WSL2 使用，原生 Windows 支持有限。  
- 部分终端（如 KDE konsole）需调整 `TERM` 变量或使用 `--direct-color` 选项优化颜色显示。