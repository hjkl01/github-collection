
---
title: reinstall
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/bin456789/reinstall?style=social) ](https://github.com/bin456789/reinstall)
### [bin456789 reinstall](https://github.com/bin456789/reinstall)

**项目核心内容总结：**

该项目是一个用于自动化安装 Windows 系统的脚本工具，支持多种版本的 Windows（包括 Windows 7、Windows 10/11、Windows Server 等）以及 ARM 架构系统。主要功能包括自动下载 ISO 镜像、安装系统、配置 SSH 密钥等，适用于云服务器和虚拟化环境。

**使用方法：**

- 通过 `--image-name` 参数指定要安装的系统版本（映像名称）；
- 使用 `--ssh-key` 添加 SSH 公钥以实现无密码登录；
- 支持从 GitHub 获取旧版本脚本以解决兼容性问题；
- 可通过 `--force-boot-mode bios` 等参数解决特定硬件兼容性问题。

**主要特性：**

- 支持多种云平台（如 Azure、AWS、阿里云、GCP 等）；
- 支持 ARM 架构的 Windows 安装；
- 自动化安装流程，减少手动操作；
- 提供常见问题的解决方法，如 GCP 上的安装问题、Windows 10 LTSC 的 CPU 占用问题等；
- 可自定义脚本，支持 Fork 仓库并修改配置。

**注意事项：**

- 部分旧系统（如 Vista、Windows 7）可能缺少驱动；
- 安装 Windows 7 时需注意 EFI 引导和虚拟机类型；
- 部分云平台（如 Google Cloud）可能需要手动加载驱动。