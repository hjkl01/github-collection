
---
title: iroh
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/n0-computer/iroh?style=social) ](https://github.com/n0-computer/iroh)
### [n0-computer iroh](https://github.com/n0-computer/iroh)

**核心内容总结：**  
Iroh 是一个基于 QUIC 协议的网络通信库，提供通过公钥拨号的 API，自动寻找并维护最快连接（支持打洞和中继服务器回退），适用于跨网络设备的高效通信。  

**主要功能与特性：**  
1. **网络连接优化**：自动尝试直接连接（打洞），失败时回退到公共中继服务器，确保连接速度。  
2. **QUIC 协议支持**：使用 Quinn 实现 QUIC，提供加密、流优先级、多路复用等特性，避免阻塞。  
3. **协议扩展性**：集成现有协议（如 iroh-blobs 内容分发、iroh-gossip 聊天网络、iroh-docs 数据存储等），无需自行开发。  
4. **跨语言支持**：主要通过 Rust 库实现，其他语言可通过 FFI 绑定使用。  

**使用方法：**  
- **Rust 库**：通过 `cargo add iroh` 安装，示例代码包含客户端连接和服务器端回显协议实现。  
- **现有协议**：可直接使用 iroh-blobs、iroh-gossip 等预构建协议。  
- **其他语言**：参考 iroh-ffi 的 FFI 绑定。  

**许可证**：Apache 2.0 或 MIT 双许可。