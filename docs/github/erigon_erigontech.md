### [erigontech erigon](https://github.com/erigontech/erigon)  ![GitHub Repo stars](https://img.shields.io/github/stars/erigontech/erigon?style=social)

Erigon 是一款专注于效率的以太坊执行层客户端，内置嵌入式共识层。主要功能包括：

1. 快速初始同步，大幅缩短全节点同步时间。
2. 高效状态存储，使用扁平 KV 数据库、预处理及不可变快照，支持低成本磁盘存储历史数据。
3. 多模式配置，支持档案节点、全节点及最小节点模式。
4. 多链支持，兼容 Ethereum、Gnosis、Polygon 等网络。
5. 模块化架构，组件（如 JSON-RPC、TxPool）可独立运行，支持 Docker 部署。
6. 验证器功能，支持 PoS 块生产与验证。
7. 可观测性，提供 JSON-RPC 接口及 Grafana 监控面板。