### [lucasgelfond zerobrew](https://github.com/lucasgelfond/zerobrew)  ![GitHub Repo stars](https://img.shields.io/github/stars/lucasgelfond/zerobrew?style=social)

zerobrew 是一个面向 macOS 和 Linux 的 Homebrew 性能优化客户端，采用 uv 风格架构。它通过内容寻址存储去重和 APFS 克隆文件实现零开销复制，大幅提升包安装速度。该项目复用 Homebrew 公式与基础设施，支持包的安装、卸载、Brewfile 管理及直接运行，目前处于实验阶段，建议与 Homebrew 并行使用。