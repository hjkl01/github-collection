
---
title: wsldl
---

### [yuk7 wsldl](https://github.com/yuk7/wsldl)

**项目核心内容总结：**

wsldl 是一个用于管理 Windows Subsystem for Linux（WSL）发行版的工具，支持安装、启动、配置和备份 WSL 实例。其主要功能包括：

**1. 功能**  
- **安装方式多样化**：支持通过预构建发行版包、自定义 rootfs tarball（需解包到根目录）或 WSL2 的 ext4 vhdx 磁盘镜像进行安装。  
- **启动器功能**：可作为已安装 WSL 实例的启动器，通过重命名 `wsldl.exe` 文件为实例名实现。  
- **配置管理**：支持设置默认用户、终端类型（如 Windows Terminal）、是否挂载 Windows 驱动器、WSL 版本（1/2）等。  
- **备份与恢复**：可导出为 `.tar.gz`、`.ext4.vhdx.gz` 等格式，或导入备份文件恢复实例。  
- **卸载功能**：通过 `clean` 命令卸载指定实例。

**2. 使用方法**  
- **安装预构建发行版**：下载 `wsldl.exe`，重命名为目标实例名（如 `Ubuntu-20.04.exe`），并确保安装文件（tarball 或 vhdx）与 exe 同目录后运行。  
- **启动实例**：直接运行 `实例名.exe` 打开终端，或使用 `run`/`runp` 执行命令（支持路径转换）。  
- **配置参数**：通过 `config` 命令设置默认用户、终端类型等，`get` 命令可查询当前配置。  
- **备份与恢复**：使用 `backup` 导出备份文件，`install` 导入备份文件恢复实例。

**3. 主要特性**  
- 兼容 WSL1 和 WSL2。  
- 支持自定义用户 UID 和默认终端（如 Windows Terminal）。  
- 提供路径转换功能（Windows 路径转为 Linux 路径）。  
- 可通过命令行直接操作实例（如运行命令、卸载、备份）。  
- 支持跨平台安装（x64/arm64）。  

**要求**：需 Windows 10 1709 及以上版本，且已启用 WSL 功能。