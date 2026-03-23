### [tursodatabase agentfs](https://github.com/tursodatabase/agentfs)  ![GitHub Repo stars](https://img.shields.io/github/stars/tursodatabase/agentfs?style=social)

AgentFS 是面向 AI 代理的文件系统，基于 SQLite 将文件、状态与工具调用记录存入单一数据库，提供可审计、可快照复现、可移植的代理运行时存储。项目包含 TypeScript/Python/Rust SDK 与 CLI，支持 POSIX 类文件系统、键值存储和工具调用审计接口，可查询历史、回滚状态，并通过 FUSE/NFS 挂载到主机或在沙盒中运行。