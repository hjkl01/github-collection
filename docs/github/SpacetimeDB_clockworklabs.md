### [clockworklabs SpacetimeDB](https://github.com/clockworklabs/SpacetimeDB)  ![GitHub Repo stars](https://img.shields.io/github/stars/clockworklabs/SpacetimeDB?style=social)

SpacetimeDB 是一个关系型数据库兼服务器系统。开发者可将应用逻辑模块直接写入数据库，客户端无需中间层即可直接连接。核心特性包括：

1. **零基础设施管理**：无需部署 Web 服务器、容器或 K8s，应用逻辑与数据在单一二进制中运行。
2. **实时状态同步**：客户端订阅数据库表，数据变更时自动推送更新，无需轮询。
3. **多语言支持**：服务端逻辑支持 Rust、C#、TypeScript、C++，客户端提供对应 SDK。
4. **高性能与一致性**：提供 ACID 保证，数据驻留内存以低延迟运行，同时具备磁盘持久化能力。
5. **内置权限控制**：所有业务逻辑、认证及授权规则均直接定义在数据库模块中。