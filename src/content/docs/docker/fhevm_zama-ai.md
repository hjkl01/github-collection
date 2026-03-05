
---
title: fhevm
---

### [zama-ai fhevm](https://github.com/zama-ai/fhevm)  ![GitHub Repo stars](https://img.shields.io/github/stars/zama-ai/fhevm?style=social)

FHEVM 是 Zama 机密区块链协议的核心框架，允许在 EVM 兼容链上利用全同态加密（FHE）创建机密智能合约。

**主要功能：**
*   **隐私保障**：实现交易和状态的端到端加密，数据在链上处理时保持加密，且不破坏与现有公开 dApp 的兼容性。
*   **易用性**：使用标准 Solidity 编写，兼容现有工具链，开发者无需精通密码学。
*   **计算能力**：支持 256 位精度加密整数及全套运算操作符，通过符号执行和异步协处理器实现高效处理。
*   **安全性**：底层加密抗量子，密钥管理采用多方计算（MPC），防止单点故障。
*   **应用范围**：支持机密转账、盲拍、游戏、投票及加密身份等场景。