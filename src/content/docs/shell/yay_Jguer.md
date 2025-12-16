
---
title: yay
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/Jguer/yay?style=social) ](https://github.com/Jguer/yay)
### [Jguer yay](https://github.com/Jguer/yay)

### 核心内容总结

**项目功能**  
Yay 是一个用 Go 编写的 AUR（Arch User Repository）助手，用于简化 Arch Linux 及其衍生发行版中 AUR 包的安装与管理。

**主要特性**  
- 支持高级依赖解析与自动下载 PKGBUILD（来自 ABS 或 AUR）；  
- 提供 AUR 包搜索、筛选、安装及升级功能；  
- 支持构建本地 PKGBUILD 并处理依赖；  
- 可生成开发版（`-git`）包数据库，升级开发版软件；  
- 支持对 AUR 包进行投票、取消投票；  
- 提供安装前交互式确认、构建后清理无用依赖等优化功能。

**使用方法**  
1. **安装**  
   - **源码安装**：通过 AUR 克隆仓库并编译（需 `git` 和 `base-devel`）：  
     ```sh  
     sudo pacman -S git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si  
     ```  
   - **二进制安装**：使用预编译的 `yay-bin` 包：  
     ```sh  
     sudo pacman -S git base-devel && git clone https://aur.archlinux.org/yay-bin.git && cd yay-bin && makepkg -si  
     ```  
   - **其他发行版**：若使用 Manjaro 等已集成 Yay 的系统，可通过 `pacman` 安装：  
     ```sh  
     pacman -S yay  
     ```  

2. **常用操作**  
   - 升级系统：`yay -Syu`；  
   - 安装 AUR 包：`yay <包名>`；  
   - 生成开发包数据库：`yay -Y --gendb`；  
   - 升级开发版包：`yay -Syu --devel`；  
   - 构建本地 PKGBUILD：`yay -Bi <目录>`；  
   - 下载 PKGBUILD：`yay -G <AUR包名>`。  

**注意事项**  
- 需确保 `/etc/pacman.conf` 中启用 `Color` 选项以支持彩色输出；  
- 若 `git` 包未被正确识别，需运行 `yay -Y --gendb` 生成开发包数据库；  
- 被标记为“过时”的 AUR 包需联系维护者更新 `PKGBUILD`，Yay 不会自动处理；  
- 问题反馈需通过 GitHub Issues，而非 Arch 论坛或 AUR 评论。