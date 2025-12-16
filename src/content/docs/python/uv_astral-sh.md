
---
title: uv
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/astral-sh/uv?style=social) ](https://github.com/astral-sh/uv)
### [astral-sh uv](https://github.com/astral-sh/uv)

**uv 项目核心内容总结：**

uv 是一个用 Rust 编写的 Python 包和项目管理工具，旨在替代 pip、pip-tools、poetry 等工具，具备以下核心功能和特性：

### **主要功能**
1. **快速依赖管理**：比 pip 快 10-100 倍，支持依赖解析、锁定和同步。
2. **项目管理**：支持初始化项目、添加依赖、生成锁文件（平台无关的 requirements 文件）。
3. **脚本与工具集成**：可运行脚本、安装第三方工具（如 black、flake8 等）。
4. **Python 版本管理**：支持安装、切换 Python 版本，通过 `.python-version` 文件进行版本锁定。
5. **兼容 pip 工作流**：提供 `uv pip` 接口，兼容 pip、pip-tools 命令，如 `pip compile`、`pip sync`。

### **使用方法**
- **安装**：通过 `curl` 安装（如 `curl -L https://astral.sh/uv/install.sh | sh`），或使用 `pip install uv`。
- **项目操作**：
  - 初始化项目：`uv init`。
  - 添加依赖：`uv add package_name`。
  - 生成锁文件：`uv pip compile requirements.in --universal --output-file requirements.txt`。
  - 安装依赖：`uv pip sync requirements.txt`。
- **Python 版本管理**：`uv python pin 3.11` 锁定版本，`uv python install 3.11` 安装指定版本。

### **主要特性**
- **高性能**：基于 PubGrub 依赖解析器，优化依赖解析速度。
- **统一锁文件**：使用 `uv.lock` 文件实现跨平台、可复现的依赖管理。
- **工作区支持**：类似 Cargo 的工作区机制，管理多项目依赖。
- **磁盘优化**：通过全局缓存减少重复下载，节省磁盘空间。
- **兼容性**：提供与 pip 兼容的接口，便于迁移和集成现有流程。

### **适用场景**
适用于需要快速构建 Python 项目、管理复杂依赖、多版本 Python 开发的场景，尤其适合对性能和可复现性有要求的团队。