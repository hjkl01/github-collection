
---
title: ic
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/dfinity/ic?style=social) ](https://github.com/dfinity/ic)
### [dfinity ic](https://github.com/dfinity/ic)

**核心内容总结：**

**项目功能**  
Internet Computer（IC）是首个以Web速度运行且可无限扩展的区块链，采用类似TCP/IP协议的架构，支持去中心化应用开发。其核心功能包括：  
- 通过无界容量扩展支持大规模应用  
- 基于新型密码学（如非交互式分布式密钥生成）实现无需挖矿的共识机制  
- 内置去中心化治理系统（Network Nervous System，NNS）管理网络升级和资源分配  

**使用方法**  
1. **开发者**：使用DFINITY提供的Canister SDK快速部署本地测试环境（<2分钟启动）。  
2. **研究者**：通过协议文档（如共识机制、Token经济学）及接口规范（IC Interface Specification）深入理解协议设计。  
3. **节点提供者**：参考Wiki文档参与网络节点运行，无需传统挖矿。  
4. **生态构建者**：基于接口规范开发SDK、钱包等工具。  

**主要特性**  
- **技术架构**：模块化设计（GuestOS/HostOS/SetupOS），支持Rust语言实现的Replica节点。  
- **验证机制**：提供代码构建与发布版本的完整性验证流程（通过repro-check脚本）。  
- **开源政策**：Apache 2.0授权，部分组件采用更严格的社区源代码许可。  
- **资源管理**：通过NNS提案系统（如https://github.com/dfinity/nns-proposals）实现去中心化决策。  

**构建要求**  
需Ubuntu 22.04+系统、16GB内存、Podman环境，支持容器化编译（`./ci/container/build-ic.sh`）。