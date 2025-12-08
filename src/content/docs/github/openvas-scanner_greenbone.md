
---
title: openvas-scanner
---

### [greenbone openvas-scanner](https://github.com/greenbone/openvas-scanner)

**核心内容总结：**  
OpenVAS Scanner 是 Greenbone 社区版的漏洞扫描引擎，用于 Greenbone 企业设备，支持持续更新的漏洞测试（VTs）。  

**功能与特性：**  
- 提供完整的扫描功能，集成最新漏洞检测规则；  
- 支持通过 CMake 编译安装，或使用 Docker 镜像部署；  
- 包含 Rust 语言实现的替代方案，旨在简化扫描器使用并集中功能；  
- 提供 Docker 镜像构建方式及容器化部署方案（当前处于开发阶段）。  

**使用方法：**  
- 安装：`cmake .` + `make install`，或通过 Docker 构建镜像；  
- 社区用户可使用 Greenbone 提供的虚拟机（TestNow）快速部署；  
- Rust 实现需参考 `rust/README.md`。  

**其他：**  
- 项目由 Greenbone AG 维护，支持通过社区门户或 GitHub 提交问题；  
- 代码部分采用 GPL v2 许可，Rust 实现附加 MIT 许可。