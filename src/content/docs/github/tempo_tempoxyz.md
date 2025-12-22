
---
title: tempo
---

### [tempoxyz tempo](https://github.com/tempoxyz/tempo)  ![GitHub Repo stars](https://img.shields.io/github/stars/tempoxyz/tempo?style=social)

**Tempo项目核心内容总结**  

**项目功能**  
Tempo是一个专为大规模稳定币支付设计的区块链，支持高吞吐量、低成本交易，兼容EVM（以太坊虚拟机），并提供金融机构和支付平台所需的现代支付基础设施功能。  

**主要特性**  
1. **TIP-20代币标准**：支持专用支付通道、跨链数据传输及合规性政策（TIP-403）。  
2. **低费用**：用户用稳定币支付Gas费，费用低于0.001美元。  
3. **Tempo交易**：支持批量支付、费用赞助、定时转账及生物识别认证。  
4. **性能**：基于Reth SDK实现高性能EVM，采用Simplex共识机制（<1秒最终性）。  
5. **兼容性**：完全兼容EVM（Osaka硬分叉），支持Solidity、Foundry等工具。  

**使用方法**  
- **用户**：通过测试网连接信息（链ID 42429，RPC地址等）接入，使用Faucet获取测试代币。  
- **操作员**：通过预编译二进制、源码构建或Docker安装节点。  
- **开发者**：使用TypeScript、Rust、Go或Foundry SDK开发，可通过`just`工具构建和测试代码。  

**其他**  
支持未来功能包括多币种费用支付及隐私代币标准，当前处于审计阶段，暂无漏洞赏金计划。