
---
title: libsignal
---

### [signalapp libsignal](https://github.com/signalapp/libsignal)  ![GitHub Repo stars](https://img.shields.io/github/stars/signalapp/libsignal?style=social)

**项目核心内容总结：**

**1. 项目功能**  
libsignal 是 Signal 客户端和服务器使用的加密库，提供跨平台 API（Java/Android、Swift/iOS、TypeScript/Desktop），底层用 Rust 实现。包含以下模块：  
- **libsignal-protocol**：实现 Signal 协议（如 Double Ratchet 算法）  
- **signal-crypto**：加密原语（如 AES-GCM）  
- **设备传输、零知识群组（zkgroup）、远程认证（attest）** 等功能模块  
- 支持 PIN 密码、用户名生成、媒体处理等  

**2. 使用方法**  
- **构建依赖**：需安装 Rust、Clang、CMake、Protobuf 编译器等工具。Linux/Debian 可通过 `apt` 安装依赖，macOS 可运行脚本 `bin/mac_setup.sh`。  
- **Java/Android**：需 JDK 17、Android NDK/SDK，通过 `./gradlew build` 构建，支持 Maven 依赖（需配置仓库地址）。  
- **Swift**：详见 `swift/README.md`。  
- **Node.js**：需 Node.js 和 npm，通过 `npm run build` 构建，支持 NPM 包 `@signalapp/libsignal-client`。  

**3. 主要特性**  
- **跨平台支持**：Java/Android、Swift/iOS、TypeScript/Desktop  
- **加密安全**：基于 Rust 实现，支持零知识证明、HSM 远程认证等高级功能  
- **模块化设计**：各功能模块独立，可灵活集成  
- **版本控制**：API 变更可能影响兼容性，版本号与工具版本绑定  

**4. 贡献与法律**  
- 接受外部贡献，需先讨论并签署 CLA  
- 使用 **GNU AGPLv3** 许可证  
- **加密软件出口限制**：需遵守所在国家法律法规（如美国 ECCN 5D002.C.1 分类）  

**5. 其他**  
- 旧版本通过 Maven Central 发布，0.86.6 后迁移至新仓库  
- 构建时可启用调试日志或额外检查（如 `-P debugLevelLogs`）