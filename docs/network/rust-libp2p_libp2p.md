### [libp2p rust-libp2p](https://github.com/libp2p/rust-libp2p)  ![GitHub Repo stars](https://img.shields.io/github/stars/libp2p/rust-libp2p?style=social)

该仓库是 libp2p 网络规范在 Rust 上的核心实现，用于构建点对点 (P2P) 网络通信。它提供了完整的底层网络协议栈，主要功能模块包括核心传输与流复用接口 (`core/`)、传输协议与升级 (`transports/`)、流复用实现 (`muxers/`)、Swarm 网络管理 (`swarm/`) 以及应用协议实现 (`protocols/`)。开发者可利用这些组件构建分布式应用程序，仓库也包含丰富的示例代码。