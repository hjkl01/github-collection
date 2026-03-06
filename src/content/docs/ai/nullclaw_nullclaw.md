
---
title: nullclaw
---

### [nullclaw nullclaw](https://github.com/nullclaw/nullclaw)  ![GitHub Repo stars](https://img.shields.io/github/stars/nullclaw/nullclaw?style=social)

NullClaw 是一个使用 100% Zig 编写的超轻量级全自主 AI 助手基础设施。项目核心功能与特点如下：

1. **极致轻量**：678 KB 静态二进制文件，无运行时依赖，峰值内存约 1 MB，启动时间小于 2 毫秒，可在低至 5 美元的硬件上运行。
2. **高度可移植**：支持 ARM、x86、RISC-V 架构，所有子系统（AI 提供商、通信渠道、工具、内存等）均采用 vtable 接口设计，支持灵活配置替换且无需修改代码。
3. **功能全面**：内置 23+ AI 模型提供商、18+ 通信渠道（如 Telegram、Discord、WhatsApp 等）、18+ 工具（如 Shell、文件操作、硬件外设）及混合向量检索记忆系统。
4. **安全设计**：提供多层沙箱隔离、密钥加密、访问白名单、资源限制及审计日志，确保系统全层安全。
5. **灵活部署**：支持 CLI 交互、Gateway API、后台服务管理及边缘部署（WASM），配置格式兼容 OpenClaw。