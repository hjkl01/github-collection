
---
title: bore
---

### [ekzhang bore](https://github.com/ekzhang/bore)

### **bore：高效、简洁的TCP隧道工具**

**功能概述**  
bore 是一个基于 **Rust** 编写的现代 TCP 隧道工具，能够将本地端口暴露到远程服务器，从而绕过标准 NAT 防火墙。其设计**简洁高效**，专注于实现核心功能，无多余附加特性。

**主要特性**  
- **安全通信**：使用 **TLS 加密** 所有通信，支持 **密钥认证** 和 **无认证** 两种方式，确保连接安全性。  
- **灵活配置**：  
  - 允许用户通过 `--port` 选项指定远程服务器的端口，或使用 `--local-host` 指定本地主机地址。  
  - 支持自托管服务器，可为控制服务器和隧道指定不同 IP 地址，满足复杂网络需求。  
- **协议设计**：  
  - 客户端与服务器之间通过 **TLS 加密连接**，初始交换 `HELLO` 消息，包含客户端公钥。  
  - 服务器生成会话密钥并使用客户端公钥加密后发送，客户端解密后用于后续通信。  

**使用方法**  
- **本地转发**：  
  ```bash  
  bore local <本地端口> --to <远程服务器地址>  
  ```  
  示例：  
  ```bash  
  bore local 8000 --to bore.pub  
  ```  
  该命令将本地 8000 端口暴露到 `bore.pub` 的随机端口。  

- **自托管服务器**：  
  ```bash  
  bore server  
  ```  
  启动后，用户可通过 `--to <地址>` 将本地端口转发到该服务器。  

**安装方式**  
- **Rust 项目**：  
  ```bash  
  cargo install bore-cli  
  ```  
- **包管理器**：  
  - macOS：`brew install bore-cli`  
  - Arch Linux：`yay -S bore`  
  - Gentoo：通过 `gentoo-zh` 覆盖层安装 `net-proxy/bore`  
- **Docker**：  
  ```bash  
  docker run -it --init --rm --network host ekzhang/bore <参数>  
  ```  

**开发与协作**  
- **测试与构建**：  
  ```bash  
  cargo test  # 运行测试  
  cargo build  # 构建项目  
  ```  
- **贡献方式**：欢迎提交 **Pull Request** 和 **Issue 报告**，详见 [CONTRIBUTING.md](https://github.com/ekzhang/bore/blob/main/CONTRIBUTING.md)。  

**许可与支持**  
- **许可**：MIT 许可协议，详见 [LICENSE](https://github.com/ekzhang/bore/blob/main/LICENSE)。  
- **支持**：由 **Ekrem Kocak** 和 **Rust Foundation** 共同维护。  

**作者信息**  
由 [Ekrem Kocak](https://github.com/ekzhang) 编写，如需联系作者，请访问其 GitHub 仓库。  

---  
**核心价值**：bore 以简洁、安全、高效为核心，为开发者提供了一个轻量级的 TCP 隧道解决方案，适用于需要快速暴露本地服务的场景。