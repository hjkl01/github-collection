
---
title: ore
---

### [ ![GitHub Repo stars](https://img.shields.io/github/stars/regolith-labs/ore?style=social) ](https://github.com/regolith-labs/ore)
### [regolith-labs ore](https://github.com/regolith-labs/ore)

ORE 是一个加密货币挖矿协议，支持挖矿、质押和管理员操作等功能。项目提供模块化指令结构，包含以下核心功能：

1. **挖矿指令**：支持自动化配置、收益结算、SOL/ORE奖励领取、棋盘重置等操作。
2. **质押指令**：允许用户存款、提现及领取质押收益，包含Seeker代币认领功能。
3. **管理指令**：提供管理员权限转移、费用配置、SOL封装等控制功能。

**状态管理**：通过多个结构体跟踪自动化配置、棋盘轮次、矿工状态、资金池等关键数据。

**使用方法**：  
- 运行测试用例：`cargo test-sbf`  
- 生成代码覆盖率报告：`cargo llvm-cov`  

主要特性包括模块化指令设计、多角色操作支持（矿工/质押者/管理员）、完整的状态追踪系统及可扩展的配置管理。