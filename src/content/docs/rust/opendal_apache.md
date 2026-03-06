
---
title: opendal
---

### [apache opendal](https://github.com/apache/opendal)  ![GitHub Repo stars](https://img.shields.io/github/stars/apache/opendal?style=social)

Apache OpenDAL 是一个开源统一数据访问层项目，遵循“一层覆盖所有存储”的核心理念。它提供统一的接口，实现与多样化存储服务的无缝交互。

核心功能特性：
1. **多语言支持**：提供 Rust 核心库，并支持 C、C++、Go、Java、Python、Node.js 等多种语言的绑定接口。
2. **多种接入方式**：支持命令行工具访问、POSIX 文件系统 API 调用，以及作为其他框架（如 Parquet、Object Store）的后端集成。
3. **广泛存储服务兼容**：涵盖对象存储、文件存储、标准协议、云盘、键值存储、数据库及缓存服务等数十种存储后端（如 S3、Redis、MySQL 等）。