### [yuk7 wsldl](https://github.com/yuk7/wsldl)  ![GitHub Repo stars](https://img.shields.io/github/stars/yuk7/wsldl?style=social)

wsldl 是一款高级的 WSL（Windows 子系统 Linux）发行版启动器与安装工具。

主要功能：
1. 安装发行版：支持通过预构建包、rootfs tarball 或 ext4 vhdx 镜像（WSL2）进行安装，可通过重命名 exe 注册自定义实例名称。
2. 启动实例：作为已安装发行版的启动器，支持默认启动 Shell 或运行指定命令（含 Windows 路径转换）。
3. 配置管理：支持通过命令行配置默认用户、UID、PATH 策略、驱动器挂载、WSL 版本及终端类型。
4. 数据维护：支持实例数据备份（tar/vhdx 等格式）、从备份恢复安装以及卸载实例。

运行环境：Windows 10 1709 及以上版本 (x64/arm64)，需启用 WSL 功能。