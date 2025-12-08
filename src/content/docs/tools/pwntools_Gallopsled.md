
---
title: pwntools
---

### [Gallopsled pwntools](https://github.com/Gallopsled/pwntools)

**项目功能**：pwntools 是一个用于 CTF 比赛的 Python 框架和漏洞利用开发库，旨在简化漏洞利用代码的编写，支持快速原型设计。  
**使用方法**：通过 Python 脚本实现远程连接、汇编代码生成、Shellcode 注入等操作，例如示例中通过 `remote` 连接目标服务，使用 `asm` 和 `shellcraft.sh()` 生成并发送 Shellcode。  
**主要特性**：  
1. 提供丰富的工具函数（如汇编、反汇编、网络通信、调试等）；  
2. 支持多种架构（如 i386、x86_64）和操作系统（如 Linux、Windows）；  
3. 依赖 Python 3.10+，兼容主流 Posix 系统（Ubuntu、Debian、FreeBSD 等）；  
4. 配套完整文档、教程及 CTF 题解示例；  
5. 社区活跃，提供 Discord 技术支持。