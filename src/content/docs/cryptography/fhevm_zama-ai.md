
---
title: fhevm
---

### [zama-ai fhevm](https://github.com/zama-ai/fhevm)

**FHEVM 核心内容总结**  

### **项目功能**  
FHEVM 是 Zama Confidential Blockchain Protocol 的核心框架，通过全同态加密（FHE）技术，实现 EVM 兼容区块链上的保密智能合约。支持加密数据在链上直接处理，确保交易和状态的端到端加密，同时保持与现有 dApp 的兼容性。  

### **主要特性**  
1. **隐私设计**：通过 FHE 实现数据加密，保障 Ethereum 上去中心化应用的隐私与保密性。  
2. **Solidity 集成**：支持使用 Solidity 编写 FHEVM 合约，兼容 Hardhat 和 Foundry 等工具链。  
3. **高精度加密**：支持 256 位精度的加密整数运算，涵盖加减乘除、比较、布尔运算等操作。  
4. **安全性**：基于量子抗性 FHE 方案，结合多方计算（MPC）的密钥管理，确保安全性。  
5. **高效执行**：通过宿主链的符号执行和异步分发至协处理器，提升计算效率。  

### **使用方法**  
- **开发**：使用 Solidity 编写合约，集成 FHEVM 工具链（如 Hardhat）。  
- **部署**：通过 `gateway-contracts` 和 `host-contracts` 管理链上与链下组件交互。  
- **测试**：利用 `test-suite` 和 Docker Compose 进行端到端测试。  

### **典型应用场景**  
- 保密转账（隐藏余额与金额）  
- 代币化与 RWAs 交易（隐藏交易金额）  
- 盲拍卖（隐藏出价与中标者）  
- 链上游戏（隐藏策略与选择）  
- 保密投票（防止贿赂与威胁）  
- 加密 DID（隐私存储身份信息）  

### **资源与支持**  
- **文档**：[Zama 官方文档](https://docs.zama.ai/protocol)  
- **白皮书**：[FHEVM 白皮书](https://github.com/zama-ai/fhevm/blob/main/fhevm-whitepaper.pdf)  
- **社区支持**：[Zama 社区](https://zama.ai/community)  
- **许可证**：[BSD-3-Clause-Clear](LICENSE)  

### **贡献与许可**  
- 商业使用需购买 Zama 专利许可（开发、研究用途免费）。  
- 贡献方式：提交 GitHub 问题或联系 hello@zama.ai 成为官方贡献者。