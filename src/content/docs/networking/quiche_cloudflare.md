
---
title: quiche
---

### [cloudflare quiche](https://github.com/cloudflare/quiche)

**项目核心内容总结：**  
quiche 是一个实现 QUIC 传输协议和 HTTP/3 的 Rust 库，提供低级别 API 用于处理 QUIC 数据包和连接状态，需由应用层自行管理 I/O 和事件循环。  

**功能与特性：**  
1. **协议支持**：完整支持 QUIC 和 HTTP/3，基于 BoringSSL 实现 TLS 加密握手。  
2. **跨平台兼容**：支持 Android、iOS、Linux 等平台，提供 C/C++ 绑定（通过 FFI 接口）。  
3. **灵活配置**：允许自定义连接参数（如流控窗口、加密设置等），支持 OpenSSL 替代实现（需禁用 0-RTT）。  
4. **开发工具**：包含示例代码（如 C/C++ 集成示例）、Docker 镜像及测试套件。  

**使用方法：**  
- **构建**：需 Rust 1.85+，通过 `cargo build` 编译，依赖 BoringSSL（自动构建）或 OpenSSL。  
- **运行示例**：使用 `cargo run --example <示例名称>` 启动客户端/服务器。  
- **C/C++ 集成**：启用 `ffi` 特性后，链接静态库 `libquiche.a`，调用 C API。  
- **移动端构建**：Android 需 NDK 19+ 及 `cargo-ndk`，iOS 需 `cargo-lipo` 生成脂肪二进制。  

**注意事项**：  
- 构建需安装 cmake、NASM（Windows）等工具。  
- Android/iOS 需配置对应工具链及 Rust 目标架构。