
---
title: ecapture
---

### [gojue ecapture](https://github.com/gojue/ecapture)

**项目核心内容总结：**

eCapture 是一个基于 eBPF 技术的开源工具，用于在不依赖 CA 证书的情况下捕获和解密 TLS 加密流量的明文数据。其主要功能包括：

- **支持多种协议和语言**：支持 OpenSSL、GoTLS 等协议，适用于 HTTPS、HTTP 等流量的解密。
- **三种捕获模式**：
  - **PcapNG 模式**：将流量保存为 `.pcapng` 文件，使用 Wireshark 或 Tshark 可以查看明文内容。
  - **Keylog 模式**：记录 TLS 的 Master Secret 信息，用于后续解密。
  - **Text 模式**：直接输出明文数据到终端。
- **支持多种模块**：除 TLS 外，还支持 Bash、MySQL、PostgreSQL 等模块的数据捕获。
- **图形化界面**：eCaptureQ 是 eCapture 的图形化客户端，支持跨平台（Windows/macOS/Linux），提供直观的实时流量分析界面。
- **使用方法**：
  - 使用命令行工具（如 `ecapture tls`、`ecapture gotls` 等）进行流量捕获。
  - 支持通过 HTTP 接口更新配置。
- **主要特性**：
  - 不依赖 CA 证书即可解密 TLS 流量。
  - 支持实时捕获和分析。
  - 提供 `.pcapng` 文件和日志文件，便于后续分析。
  - 与 Wireshark、Tshark 等工具兼容，支持实时解密显示。

**项目功能总结：**  
eCapture 是一个基于 eBPF 的加密流量分析工具，用于捕获和解密 TLS 加密通信的明文数据，适用于多种场景（如 HTTPS、GoTLS 等），支持命令行和图形化界面操作，便于网络流量分析与调试。