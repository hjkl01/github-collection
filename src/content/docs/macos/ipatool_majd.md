
---
title: ipatool
---

### [majd ipatool](https://github.com/majd/ipatool)  ![GitHub Repo stars](https://img.shields.io/github/stars/majd/ipatool?style=social)

**IPATool 核心内容总结：**

**项目功能：**  
IPATool 是一个命令行工具，用于在苹果 App Store 上搜索 iOS 应用，并下载其安装包（IPA 文件）。

**使用方法：**  
1. **认证登录：** 使用 `ipatool auth login` 登录 App Store，需要提供 Apple ID。
2. **搜索应用：** 使用 `ipatool search` 搜索应用，可指定搜索关键词和结果数量。
3. **获取应用授权：** 使用 `ipatool purchase` 为应用获取授权（需提供应用的 Bundle Identifier）。
4. **列出应用版本：** 使用 `ipatool list-versions` 查看应用的可用版本（需提供 App ID 或 Bundle Identifier）。
5. **下载 IPA 文件：** 使用 `ipatool download` 下载应用（需提供 App ID 或 Bundle Identifier，可指定版本和输出路径）。
6. **获取版本元数据：** 使用 `ipatool get-version-metadata` 获取特定版本的详细信息。

**主要特性：**  
- 支持 Windows、Linux 和 macOS 系统。
- 支持 JSON 和文本格式的输出。
- 支持交互模式和非交互模式（自动化环境）。
- 提供 Homebrew 安装方式（macOS）。
- 可自行编译，使用 Go 语言开发。

**安装方式：**  
- 手动下载 GitHub 发布版本。
- macOS 用户可通过 Homebrew 安装：`brew install ipatool`。