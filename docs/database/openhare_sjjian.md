### [openhare](https://github.com/sjjian/openhare) ![GitHub Repo stars](https://img.shields.io/github/stars/sjjian/openhare?style=social)

openhare 是一款由 AI 驱动的跨平台桌面 SQL 客户端，面向日常开发、数据分析和 DBA 管理场景。项目核心功能包括：AI 辅助编写/优化/理解 SQL、支持 Windows/macOS/Linux、简洁易用的现代化界面、开源（Apache 2.0）以及多数据库统一连接与管理。  
支持的数据库有 MySQL、PostgreSQL、SQL Server、SQLite、Oracle、MongoDB、Redis；其中数据库驱动由 Go 实现，并通过 Dart FFI 与 Flutter 客户端集成。整体技术栈基于 Flutter，使用 Riverpod/GoRouter 做状态与路由管理，ObjectBox 做存储。