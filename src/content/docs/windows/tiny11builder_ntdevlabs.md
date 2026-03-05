
---
title: tiny11builder
---

### [ntdevlabs tiny11builder](https://github.com/ntdevlabs/tiny11builder)  ![GitHub Repo stars](https://img.shields.io/github/stars/ntdevlabs/tiny11builder?style=social)

tiny11builder 是一个基于 PowerShell 的开源项目，旨在自动化构建精简版 Windows 11 镜像。它支持任意 Windows 11 版本、语言和架构，利用 DISM 压缩技术减小 ISO 体积，并包含无人值守安装文件以跳过微软账户登录。项目提供两个主要脚本：
1. tiny11maker.ps1：常规版，移除大量预装应用和臃肿软件（如 Edge、OneDrive、Xbox 等），但保留系统可维护性，支持后续添加语言、更新和功能。
2. tiny11coremaker.ps1：精简核心版，移除更多系统组件（如组件存储、更新、Defender、WinRE），体积更小但无法维护，不适合常规使用，主要用于开发测试或虚拟机环境。
项目允许用户自定义保留或删除的内容，实现高度灵活的系统定制。