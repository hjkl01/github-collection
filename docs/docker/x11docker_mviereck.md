### [mviereck x11docker](https://github.com/mviereck/x11docker)  ![GitHub Repo stars](https://img.shields.io/github/stars/mviereck/x11docker?style=social)

x11docker 是一个在 Docker 或 Podman 容器中安全运行图形界面（GUI）应用程序及桌面环境的工具，支持 Linux 及 Windows（WSL 等）系统。

主要功能：
1. **图形界面支持**：自动启动独立 X 服务器或 Wayland 合成器，使容器内 GUI 应用能在宿主机显示，支持单应用无缝模式和完整桌面模式。
2. **安全性增强**：避免 X 协议安全漏洞，默认非 root 运行，最小化容器权限，提供沙箱环境以隔离风险。
3. **丰富特性**：支持 GPU 加速、音频、剪贴板、网络、共享目录、摄像头及打印机等硬件访问。
4. **灵活配置**：兼容多种容器后端、初始化系统和运行时环境，支持预设配置以简化常用组合。
5. **轻量便捷**：基于 Bash 脚本，依赖少，安装简单，提供完善的文档与故障排查支持。