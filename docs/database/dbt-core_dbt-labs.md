### [dbt-core](https://github.com/dbt-labs/dbt-core) ![GitHub Repo stars](https://img.shields.io/github/stars/dbt-labs/dbt-core?style=social)

dbt Core v2.0 是用 Rust 重写的数据转换工具，支持 macOS、Linux、Windows 系统。

核心功能：数据分析师和工程师通过编写 SQL SELECT 语句即可将数据转换为数据仓库中的表和视图，dbt 自动处理模型间的依赖关系管理和关系可视化。

主要特性：解析和编译速度大幅提升，采用严格的语言规范确保正确性，生成 Parquet 格式产物便于后续分析，同时保留 JSON 产物兼容旧版本。以单一自包含二进制分发，安装简便无需 Python 环境。遵循 Apache 2.0 开源协议。

该工具提供两种发行版：dbt Core（基础版，Apache 2.0 许可）和 Fusion（扩展版，含增强 SQL 理解能力）。两者共享同一语言规范，业务逻辑可双向迁移。