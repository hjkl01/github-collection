### [cross-rs cross](https://github.com/cross-rs/cross)  ![GitHub Repo stars](https://img.shields.io/github/stars/cross-rs/cross?style=social)

`cross` 是一个零设置的 Rust 交叉编译和测试工具。它依赖 Docker 或 Podman 容器提供交叉工具链和库，无需修改本地系统安装即可构建跨架构的可移植二进制文件。其命令行与 Cargo 完全兼容，支持在多种目标架构（如 Linux、Android、嵌入式等）上进行构建和测试（测试依赖 QEMU 模拟），兼容 Rust 稳定、Beta 及 nightly 通道。配置支持通过 `Cargo.toml`、`Cross.toml` 文件或环境变量实现。