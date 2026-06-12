### [litter](https://github.com/dnakov/litter) ![GitHub Repo stars](https://img.shields.io/github/stars/dnakov/litter?style=social)

Litter 是一个面向 Codex 的原生 iOS 和 Android 客户端，支持在手机上连接本地或远程服务器、管理会话，并运行智能体式（agentic）编程工作流。

项目采用跨平台架构：核心能力由共享的 Rust 模块（`codex-mobile-client`）提供，并通过 UniFFI 生成 Swift/Kotlin 绑定；iOS/Android 端主要负责 UI、权限、通知和平台 API。会话状态、流式处理、数据恢复（hydration）、服务发现和鉴权等逻辑集中在 Rust 层。

仓库包含 iOS 与 Android 应用、共享 Rust 桥接模块、上游 Codex 子模块、本地补丁及构建脚本；提供一套 Make 命令用于快速构建（iOS 真机/模拟器、Android 模拟器）、完整流水线构建、Rust 检查与测试、绑定代码生成、Xcode 工程生成和清理构建产物。

项目仍在积极开发中，欢迎小而聚焦的问题修复型贡献；采用 GPLv3 许可证，并附带针对 Apple App Store 与 Google Play 分发的额外许可。