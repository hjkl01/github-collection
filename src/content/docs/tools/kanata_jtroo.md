
---
title: kanata
---

### [jtroo kanata](https://github.com/jtroo/kanata)  ![GitHub Repo stars](https://img.shields.io/github/stars/jtroo/kanata?style=social)

**项目核心内容总结：**

Kanata 是一款跨平台（Linux、macOS、Windows）的键盘映射软件，支持多层按键功能和高级自定义（如按键触发延迟、宏定义、Unicode输入等）。用户可通过预编译的二进制文件或自行构建（需 Rust 工具链）安装。主要特性包括：  
- **可读性高的配置文件**（支持多层按键、动态/静态宏、Vim 风格的快捷键序列）；  
- **实时配置重载**，便于测试修改；  
- **跨平台支持**，兼容主流操作系统；  
- **TCP 服务器功能**，允许其他程序与 Kanata 交互（如切换层）；  
- **Interception 驱动支持**（Windows 需额外启用）。  

**使用方法**：  
1. 通过 [发布页面](https://github.com/jtroo/kanata/releases) 下载预编译版本；  
2. 或使用 Rust 构建：`cargo install kanata`（需 `sudo` 权限）；  
3. 配置文件示例见 `cfg_samples` 目录，详细说明参见 [配置指南](./docs/config.adoc)。  

**主要特性**：  
- 多层按键自定义；  
- 支持 Unicode 输出、宏定义；  
- 提供在线模拟器测试配置；  
- 支持跨平台的层切换和应用感知功能（如 `kanawin`、`qanata` 等社区项目）。