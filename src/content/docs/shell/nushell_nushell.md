
---
title: nushell
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/nushell/nushell?style=social) ](https://github.com/nushell/nushell)
### [nushell nushell](https://github.com/nushell/nushell)

**Nushell 核心内容总结**  

**项目功能**  
Nushell 是一个跨平台的新型 shell 工具，采用结构化数据处理方式（类似 PowerShell），支持通过管道（pipeline）操作结构化数据，提供文件/目录的表格化展示、数据过滤、插件扩展等功能。  

**主要特性**  
1. **结构化数据处理**：将文件、目录、进程等操作结果以表格形式呈现，支持通过命令链（如 `ls | where type == "dir" | table`）进行数据过滤和转换。  
2. **管道操作**：命令通过 `|` 连接，支持生产数据（如 `ls`）、过滤数据（如 `where`）、消费数据（如 `table`）三类操作。  
3. **文件/数据加载**：支持以结构化形式加载文件（如 `.toml`、`.json`），并可通过 `get` 命令提取字段（如 `open Cargo.toml | get package.version`）。  
4. **插件系统**：支持通过 JSON-RPC 协议扩展功能，插件可作为过滤器或数据终点（sink）使用。  

**使用方法**  
- **安装**：通过 `brew install nushell`（Linux/macOS）或 `winget install nushell`（Windows）安装，支持多种包管理器。  
- **配置**：默认配置文件路径可通过 `$nu.config-path` 查看，可自定义配置。  
- **学习资源**：提供官方文档（[Nushell 书籍](https://www.nushell.sh/book/)）、命令列表及示例（[cookbook](https://www.nushell.sh/cookbook/)）。  

**目标与支持**  
- **跨平台**：支持 Windows、macOS、Linux，兼容现有平台工具。  
- **现代可用性**：强调用户交互的现代性，采用函数式数据处理（无状态突变）。  
- **生态支持**：被 [zoxide](https://github.com/ajeetdsouza/zoxide)、[starship](https://github.com/starship/starship) 等工具官方支持。  

**许可证**  
采用 MIT 协议开源。