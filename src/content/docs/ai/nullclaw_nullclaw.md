
---
title: nullclaw
---

### [nullclaw nullclaw](https://github.com/nullclaw/nullclaw)  ![GitHub Repo stars](https://img.shields.io/github/stars/nullclaw/nullclaw?style=social)

NullClaw 是一个基于 Zig 语言开发的最轻量级完全自主 AI 助手基础设施。

**核心特性：**
1. **极致性能**：678 KB 静态二进制，内存占用约 1 MB，启动时间小于 2 毫秒，无运行时和 GC 开销。
2. **广泛兼容**：支持 ARM、x86、RISC-V 架构，可在成本极低的硬件设备上运行。
3. **功能完整**：集成 22+ AI 提供商、18+ 通讯渠道（Telegram, Discord, Nostr 等）、18+ 工具及混合记忆系统（Vector+FTS5）。
4. **高度扩展**：所有子系统（模型、渠道、内存、安全等）采用 vtable 接口设计，通过配置即可切换实现，无需修改代码。
5. **安全至上**：默认内网绑定、启动配对、文件沙盒、加密存储及审计日志。

**使用方法：**
1. **环境要求**：需使用 Zig 0.15.2 版本。
2. **构建编译**：执行 `zig build -Doptimize=ReleaseSmall` 生成二进制文件。
3. **初始化配置**：使用 `nullclaw onboard --interactive` 或指定 API Key 进行配置。
4. **运行模式**：
   - 交互聊天：`nullclaw agent`
   - 网关服务：`nullclaw gateway`
   - 后台服务：`nullclaw service install`
5. **配置管理**：修改 `~/.nullclaw/config.json` 文件（兼容 OpenClaw 结构），可自定义模型、渠道、工具及安全策略。

**开源协议**：MIT。