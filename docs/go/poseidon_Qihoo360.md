### [Qihoo360 poseidon](https://github.com/Qihoo360/poseidon)  ![GitHub Repo stars](https://img.shields.io/github/stars/Qihoo360/poseidon?style=social)

波塞冬（Poseidon）是一个基于倒排索引的海量日志搜索平台，支持在数百万亿条、数百 PB 的结构化或非结构化数据中快速检索特定字符串。系统通过 Hadoop Map/Reduce 构建索引，Golang 开发检索服务，结合元数据管理服务，数据无需额外存储且保留在 Hadoop 集群中，查询效率从数小时/天提升至秒级。主要应用于 APT 事件追踪等海量数据检索场景。